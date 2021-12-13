import sys
sys.path.insert(0, '')

import os
import json
import numpy as np
import h5py
import decord
import cv2
import moviepy.editor as mpe
from pydub import AudioSegment
from vid_sum.evaluation.generate_summary import generate_summary

def generate_video(score_path, metadata_path, video_path, duration=-1):

    # generate summaries
    all_scores = []
    with open(score_path) as f:
        data = json.loads(f.read())
        keys = list(data.keys())

        for video_name in keys:
            scores = np.asarray(data[video_name])
            all_scores.append(scores)

    all_shot_bound, all_nframes, all_positions, all_fps = [], [], [], []
    with h5py.File(metadata_path, 'r') as hdf:        
        for video_key in keys:
            video_index = video_key[6:]
            
            sb = np.array(hdf.get('video_' + video_index + '/change_points'))
            n_frames = np.array(hdf.get('video_' + video_index + '/n_frames'))
            positions = np.array(hdf.get('video_' + video_index + '/picks'))
            fps = hdf['video_' + video_index + '/fps'][()]

            all_shot_bound.append(sb)
            all_nframes.append(n_frames)
            all_positions.append(positions)
            all_fps.append(fps)

    all_summaries = generate_summary(all_shot_bound, all_scores, all_nframes, all_positions, all_fps, duration)


    # generate video
    with h5py.File(metadata_path, 'r') as hdf:
        for video_key, summary in zip(keys, all_summaries):
            
            # extract metadata
            video_name = hdf[video_key + '/video_name'][()].decode()
            audio_name = video_name[:-4] + '.mp3'   # change the extension from mp4 to mp3

            # make sure that the system can works properly
            # with both directory and single file
            if os.path.isdir(video_path):
                tmp_path = os.path.join(video_path, video_name)
            else:
                tmp_path = video_path

            video_reader = decord.VideoReader(tmp_path)
            audio_reader = AudioSegment.from_file(tmp_path, 'mp4')

            fps = video_reader.get_avg_fps()
            (frame_height, frame_width, _) = video_reader[0].asnumpy().shape

            # extract frame indices
            frame_numbers = list(np.argwhere(summary == 1).reshape(1, -1).squeeze(0))

            vid_writer = cv2.VideoWriter(
                'vid_sum/output_video/' + video_name,
                cv2.VideoWriter_fourcc(*'mp4v'),
                fps,
                (frame_width, frame_height)
            )
            summarized_audio = None

            # generate summary video and audio
            for idx in frame_numbers:
                # write video to file
                frame = video_reader[idx]
                vid_writer.write(cv2.cvtColor(frame.asnumpy(), cv2.COLOR_RGB2BGR))

                # get audio idx in seconds
                audio_start_idx, audio_end_idx = video_reader.get_frame_timestamp(idx)
                # seconds to miliseconds
                audio_start_idx = round(audio_start_idx*1000)
                audio_end_idx = round(audio_end_idx*1000)

                # concat audio segment
                if summarized_audio is None:
                    summarized_audio = audio_reader[audio_start_idx:audio_end_idx]
                else:
                    summarized_audio += audio_reader[audio_start_idx:audio_end_idx]

            # write audio to file
            summarized_audio.export('vid_sum/output_video/' + audio_name, format='mp3') 

            vid_writer.release()

            # combine video and audio
            input_video = mpe.VideoFileClip('vid_sum/output_video/'+ video_name)
            input_audio = mpe.AudioFileClip('vid_sum/output_video/' + audio_name)

            output_video = input_video.set_audio(input_audio)
            output_video.write_videofile(#
                'vid_sum/output_video/fin_' + video_name,
                codec='libx264',
                audio_codec='aac',
            )

            os.remove( 'vid_sum/output_video/' + video_name)
            os.remove( 'vid_sum/output_video/' + audio_name)

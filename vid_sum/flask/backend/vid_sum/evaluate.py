from vid_sum.video_generation.generator import generate_video
from vid_sum.video_summary.solver import Solver
from vid_sum.video_summary.data_loader import get_loader
from vid_sum.video_summary.configs import get_config
from vid_sum.feature_extraction.generate_dataset import GenerateDataset
import os
import sys

def main(video_path, duration = -1):

    '''
    Main function of video summarization
    Args:
        video_path(str): path to video file
        duration(int): duration of final video
            duration == -1: 15% of original video
            duration > 0: length of final video
    '''

    #save_path = 'output_feature/output_feature.h5'
    save_path = 'vid_sum/output_feature/' + os.path.basename(video_path)[:-4] + '.h5'

    # 1st step: feature extraction
    gen_data = GenerateDataset(video_path, save_path)
    gen_data.generate_dataset()

    # 2nd step: calculate result
    # init test config
    config = get_config(mode='test', video_type='custom_video')

    # init data loader
    train_loader = None
    test_loader = get_loader(config.mode, save_path, config.action_state_size)

    # evaluation
    solver = Solver(config, train_loader, test_loader)
    solver.build()
    solver.load_model('vid_sum/models/epoch-84.pkl')
    solver.evaluate(-1)

    # 3rd step: generate video
    # generate video
    score_path = 'vid_sum/output_feature/custom_video/scores/split' + str(config.split_index) + '/custom_video_-1.json'
    generate_video(score_path, save_path, video_path, duration)

if __name__ == "_main_":
    pass
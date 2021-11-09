import React from "react";
export const Deploy = ({ state }) => {
  return (
    <div>
      {state.article} <br/>
      { state.name} <br/>
      {state.age}
    </div>

  );
};

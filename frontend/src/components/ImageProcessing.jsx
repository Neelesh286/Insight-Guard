import React, { useState } from 'react';
import axios from 'axios';

const ImageProcessingComponent = ({ backendUrl }) => {
  const [postResponse, setPostResponse] = useState(null);

  const handlePostClick = async () => {
    try {
      const response = await axios.post(`${backendUrl}/api/image-process/`);
      setPostResponse(response.data.status);
    } catch (error) {
      console.error('Error posting image:', error);
    }
  };

  return (
    <div>
      <button onClick={handlePostClick}>Calculate CDR Ratio</button>
      {postResponse && (
        <div>
          <h3>Your Cup Disc Ratio Stats:</h3>
          <p>ID: {postResponse.id}</p>
          <p>Uploaded Image: {postResponse.uploaded_image}</p>
          <p>Disc Area: {postResponse.disc_area}</p>
          <p>Cup Area: {postResponse.cup_area}</p>
          <p>Cup/Disc Ratio: {postResponse.cupdisc_ratio}</p>
          <img src={postResponse.s3_link} alt="Processed Image" />
        </div>
      )}
    </div>
  );
};

export default ImageProcessingComponent;

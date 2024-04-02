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
    <div className='text-center bg-gray-300'>
      <button onClick={handlePostClick} className="bg-black text-[#00df9a] rounded-md font-medium py-2 px-4 mb-4 inline-block">Calculate CDR Ratio</button>
      {postResponse && (
        <div className="text-gray-950">
          <h3 className="mb-2">Your Cup Disc Ratio Stats:</h3>
          <p className="text-center text-lg font-semibold">ID: {postResponse.id}</p>
          <p className="text-center text-lg font-semibold">Uploaded Image: {postResponse.uploaded_image}</p>
          <p className="text-center text-lg font-semibold">Disc Area: {postResponse.disc_area}</p>
          <p className="text-center text-lg font-semibold">Cup Area: {postResponse.cup_area}</p>
          <p className="text-center text-lg font-semibold">Cup/Disc Ratio: {postResponse.cupdisc_ratio}</p>
          <img src={postResponse.s3_link} alt="Processed Image" className="mt-4 mx-auto" />
        </div>
      )}
    </div>
  );
    
};


export default ImageProcessingComponent;


// Disc Area: 20096

// Cup Area: 7095.574941871676

// Cup/Disc Ratio: 0.3530839441616081
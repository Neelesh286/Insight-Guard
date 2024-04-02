import { useState } from 'react';
import axios from 'axios';

const ImageUploadComponent = ({backendUrl}) => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [uploadStatus, setUploadStatus] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);
  const [resultData, setResultData] = useState(null);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setSelectedImage(file);
  };

  const handleUpload = async () => {
    if (selectedImage) {
      const formData = new FormData();
      formData.append('image', selectedImage);

      try {
        const response = await axios.post(`${backendUrl}/api/upload/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        console.log('Upload successful:', response.data);
        setUploadStatus('success');
        setErrorMessage(null); // Clear any previous error messages

        // Extract the image ID from the response
        const imageId = response.data.id;
        // Now make a GET request to fetch the result for the uploaded image
        const resultResponse = await axios.get(`${backendUrl}/api/result/${imageId}/`);
        console.log('Result:', resultResponse.data);
        setResultData(resultResponse.data);
      } catch (error) {
        console.error('Error uploading image:', error);
        if (error.response && error.response.data) {
          // If error response contains data, extract the message
          const errorMessage = error.response.data.image[0]; // Assuming the error message is in "image" field
          setErrorMessage(errorMessage);
        } else {
          setErrorMessage('Error uploading image. Please try again.');
        }
        setUploadStatus('error');
      }
    }
  };

  return (
    <div>
      <h2>Image Upload Component</h2>

      <input type="file" accept="image/*" onChange={handleImageChange} />
      <button onClick={handleUpload}>Upload Image</button>

      {uploadStatus === 'success' && (
        <div style={{ color: 'green' }}>File uploaded successfully!</div>
      )}

      {uploadStatus === 'error' && (
        <div style={{ color: 'red' }}>{errorMessage}</div>
      )}

      {resultData && (
        <div>
          <h3>Result for Uploaded Image</h3>
          <p>Status: {resultData.status}</p>
          {/* Display additional result data as needed */}
        </div>
      )}
    </div>
  );
};

export default ImageUploadComponent;

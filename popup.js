document.addEventListener('DOMContentLoaded', function () {
  document
    .getElementById('query-form')
    .addEventListener('submit', function (event) {
      event.preventDefault();
      const url = document.getElementById('url-input').value;
      const formData = new FormData();
      formData.append('url', url);

      fetch('https://5271-1-6-74-117.ngrok-free.app/summarize', {
        method: 'POST',
        body: formData,
      })
        .then((response) => {
          console.log(response);
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then((data) => {
          // Check if data is received properly
          console.log('Data received:', data);
          document.getElementById('response-container').innerHTML =
            data.text;
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    });
});

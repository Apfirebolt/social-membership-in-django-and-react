$(document).ready(function() {
    console.log('loaded message.js')

    // Open a modal here

    // Ajax call to get the message
    $.ajax({
        url: '/api/users',
        type: 'GET',
        success: function(response) {
            console.log(response);
            $('#message').text(response.message);
        },
        error: function(error) {
            console.log(error);
        }
    });
});
  
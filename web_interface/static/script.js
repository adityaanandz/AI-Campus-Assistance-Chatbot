$(document).ready(function() {
    $('#send-btn').click(function() {
        var user_input = $('#user-input').val();
        if (user_input !== "") {
            $('#chat-body').append('<div class="user-message">' + user_input + '</div>');
            $('#user-input').val('');
            scrollToBottom();
            getChatbotResponse(user_input);
        }
    });
});

function getChatbotResponse(user_input) {
    $.ajax({
        type: "POST",
        url: "/get_response",
        data: {
            user_input: user_input
        },
        success: function(data) {
            $('#chat-body').append('<div class="chatbot-message">' + data.response + '</div>');
            scrollToBottom();
        }
    });
}

function scrollToBottom() {
    $('#chat-body').scrollTop($('#chat-body')[0].scrollHeight);
}

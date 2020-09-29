$("#search__form").on("submit", function () {
    $.ajax({
        url: '/search_ajax/',
        type: 'post',
        data: {
            query: $("#search__input").val(),
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
        },
        dataType: 'json',
        success: function (data) {
            $('.good').html(data['search_ajax'])
        }
    })
    return false
});
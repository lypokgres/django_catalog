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

const buttons = $(".category__button");

buttons.on('click', function () {
    if ($(this).attr("id") === 'None') {
        $('.category__list').not($(this).next()).removeClass('show')
        $('.category__button').not($(this)).removeClass('active')
    }
    $(this).toggleClass('active')
    $(this).next().toggleClass('show')
})
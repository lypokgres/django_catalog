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
const element = $(".category__item")


// version 1.0

buttons.on('click', function (button) {
    $(this).toggleClass('active')
    for (let i = 0; i < element.length; i++) {
        if (element[i].id === button.target.id) {
            element.eq(i).toggleClass("show")
        }
    }
})

//sd

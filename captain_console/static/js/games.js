$(document.ready(function () {
    $('#search_btn').on('click', function (e) {
        e.preventDefault()
        var searchText = $('#search_Content').val();
        $.ajax( {
            url: '/games?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="Well game">
                            <a href="/games/${d.id}">
                                <img class="games-img" src="${d.firstImage}" />
                                <h4>${d.name}</h4>
                                <p>${d.description}</p>
                            </a>
                        </div>`
                });
                $('.grid-item').html(newHtml.join(''));
                $('#search_Content').val('');
            },
            error: function (xhr, status, error) {
                // TODO: show toaster
                console.error(error);

            }
        })

    })
}));
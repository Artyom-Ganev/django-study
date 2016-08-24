$(document).ready(function () {

    $('#delete_btn').click(function (e) {
        if (confirm("После удаления запись будет невозможно востановить") != true) {
            e.preventDefault();
        }
    });
});

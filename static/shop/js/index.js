$(document).ready(function () {

    $("img").click(function () {
        console.log("salam!");
    });

    // let id = $('input[name="cart"]')[0].value;
    // $('form#').click(function (e) {
    //     e.preventDefault();
    //     $.ajax({
    //         url: 'http://127.0.0.1:8000/cart/',
    //         method: 'POST',
    //         data: {
    //             'product': id
    //         },
    //         success: function (data) {
    //             alert("OK!");
    //             console.log(id + " ok shod!");
    //         },
    //         error: function (data) {
    //             alert("NOT OK!");
    //         }
    //     });
    // });
    $("form#form").on("submit", function(e) { // on requires jquery 1.7+
        e.preventDefault();
        alert("submit");
});
})



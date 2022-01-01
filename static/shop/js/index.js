$(document).ready(function () {
    $("#product_img").click(function () {
        console.log("salam!");
    });

    $("#check").click(function () {
        alert("clicked...")
        $.post("http://127.0.0.1:8000/get_date/", function (data, status) {
            alert("data: " + data);
        });
    });
});
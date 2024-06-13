const jQ11 = window.$;
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr'

jQ11(window).bind('load', function () {
    jQ11.getJSON(url, function (body) {
        const hello = body.hello;
        jQ11('DIV#hello').text(hello);
    });
});

const jQ7 = document.querySelector('header');

jQ7('DIV#add_item').click(function () {
    jQ7('ul').append('<li>Item</li>');
});

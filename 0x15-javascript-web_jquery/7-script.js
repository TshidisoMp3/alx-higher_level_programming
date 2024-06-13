const jQ9 = window.$;
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

jQ9.get(url, function (data) {
    jQ9('DIV#character').text(data.name);
});

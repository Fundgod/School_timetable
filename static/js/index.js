console.log(1);
document.getElementById('add-new-btn').onclick = function(){
    console.log(1);
    all_menus = document.getElementById('all-menus');
    console.log(all_menus);

    var request = new XMLHttpRequest();
    request.open('GET', '/js/add_menu'); // url = в мейне будет | Получаю id menu
    request.responseType = 'text';

    request.onload = function(){
        console.log('Выполнилось')
        id = request.response
        all_menus.insertAdjacentHTML('beforeend', '<div class="menu" id="menu_' + id +'"> Меню' +
         '<button onclick="btn_click(' + id +')" class="btn_menu" id="btn_' + id + '"> </button>' + '</div>')
    }
    request.send();
    //Запрос в бэк с требованием создаения нового меню в ДБ
    //Возвращение Текста для вставки из бэка


}

function btn_click(menu_id){
    console.log(menu_id);
    var request = new XMLHttpRequest();
    // Пишу как хочу, законом не запрещено (Но лучше потом через POST написать)
    request.open('GET', '/js/delete_menu/' + menu_id);

    request.onload  = function(){
        if (request.response == "Yes"){
            console.log('!!!!!!!!!!!!!!!!!!!!')

            var elem = document.getElementById('menu_' + menu_id);
            elem.parentNode.removeChild(elem);
        }
    }
    request.send();
}
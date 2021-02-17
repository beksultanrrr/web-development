let tasks = document.querySelector('.tasks');
let inputText = document.querySelector('.input-field');
let addButton = document.querySelector('.add-button');

let task = document.querySelectorAll('.task');
let deleteImage = document.querySelectorAll('.delete-img');

function addTask(){
    console.log("ok")
    if(inputText.value != null){

        let div = document.createElement("div");
        div.className="task";

        let label = document.createElement("label");
	    label.className = "task-new";

        let check = document.createElement("input");
        check.type = "checkbox";
        check.className = "task-checkbox";

        let span = document.createElement("span");
	    span.innerHTML = inputText.value;

        let image = document.createElement("img");
        image.className = "delete-img";
        image.src = "https://icons-for-free.com/iconfiles/png/512/delete+remove+trash+trash+bin+trash+can+icon-1320073117929397588.png";
        image.addEventListener('click', remove, false);

        tasks.appendChild(div);
        div.appendChild(label);
        label.appendChild(check);
        label.appendChild(span);
        div.appendChild(image);

        inputText.value = null;
    }
}

function remove(){
    this.parentNode.remove();
}



for(var i = 0; i < task.length; i++){
    deleteImage[i].addEventListener('click', remove, false);
}
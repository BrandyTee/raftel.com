let anime = [
    "One Piece",
    "Attack on Titan",
    "Naruto",
    "Jujutsu Kaisen",
    "Demon Slayer",
    "Chainsaw Man",
    "Dragon Ball",
    "Dandadan",
    "Uzumaki"
];

//Sort names in ascending order 
let sortedAnime = anime.sort();

//reference 
let input = document.getElementById("input");

//Evaluate function on key up
input.addEventListener("keyup", (e) => {
    //Loop thru above array 
    //Initiqlly remove all elements so if user erases a letter or adds new ones then clean the previous out 
    removeElements();
    for (let i of sortedAnime) {
        //Convert input to lowercase and compare with each string         
        if (
            i.toLowerCase().startsWith(input.value.toLowerCase()) && input.value != ""
        ) {
            //create li element 
            let listItem = document.createElement("li");
            //One common class name 
            listItem.classList.add("list-items");
            listItem.style.cursor = "pointer";
            listItem.setAttribute("onclick", "displayNames('" + i + "')");
            //Display matched part in bold
            let word = "<b>" + i.substr(0, input.value.length) + "</b>";
            word += i.substr(input.value.length);
            console.log(word);
            //Display the value in array
            listItem.innerHTML = word;
            document.querySelector(".list").appendChild(listItem);
        
    }
});
function displayNames(value) {
    input.value = value;
}

function removeElements(){
    //Clear all trash
    let items = document.querySelectorAll(".list-items");
    items.forEach((item) => {
        item.remove();
    });
};



//Functions 

// You can access the Flask variable `titles` here by embedding it into the JavaScript code

let number = 0;    
let length = "{{ length }}";
let title_answer = "{{ titles[number] }}";
let image_answer = "{{ images[number] }}";
    
let user_answer = document.getElementById("enter_anime"); 


function submit() {
    
    //Run conditionals
    /* if (user_answer.value != title_answer){
        user_answer.value = " ";
    } */
    /* else     
    {
        if (length < 20){
            number += 1;
            user_answer.value = " ";
        } else {
                number = 0;
                user_answer.value = " ";
        }
        
    } */
    
    
}



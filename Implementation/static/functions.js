function button_logic() {
    var use_length = document.forms["user_inputs"]["use_length"].value;
    var use_length = document.forms["user_inputs"]["use_length"].value;
    var use_lowercase = document.forms['user_inputs']["use_lowercase"].checked;
    var use_uppercase = document.forms['user_inputs']["use_uppercase"].checked;
    var use_digits = document.forms['user_inputs']["use_digits"].checked;
    var use_punctuation = document.forms['user_inputs']["use_punctuation"].checked;


    if (use_length != "" & (use_lowercase || use_uppercase || use_digits || use_punctuation)) { 
        document.getElementById('generate_button').disabled = false;
        return false;
         }  
    else{ 
        document.getElementById('generate_button').disabled = true; 
        return true;
         } 
};

function validate() {
    var x = document.getElementById("snackbar");
    var use_length = document.forms["user_inputs"]["use_length"].value;
    var use_lowercase = document.forms['user_inputs']["use_lowercase"].checked;
    var use_uppercase = document.forms['user_inputs']["use_uppercase"].checked;
    var use_digits = document.forms['user_inputs']["use_digits"].checked;
    var use_punctuation = document.forms['user_inputs']["use_punctuation"].checked;
    if (use_length == "" || use_length == null) { 
        x.className = "show";}

    else if(!use_lowercase & !use_uppercase & !use_digits & !use_punctuation){
        x.className = "show";
    }

    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
    return true;
}

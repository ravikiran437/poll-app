const num = parseInt(document.getElementById("django-number").dataset.number)
const input = document.getElementById("input");
const submit = document.getElementById("submit");

console.log(num)
submit.addEventListener("click",()=>{
    if (input.value == "") {
      alert("Please enter a Number");
    }
    const enteredNum = parseFloat(input.value);
    if( enteredNum=== num){
        alert("You Won")
    }
    else if(enteredNum > num){
        alert("Your number is Big")
    }
    else{
        alert("Your Number is small")
    }
    input.value = ""
})

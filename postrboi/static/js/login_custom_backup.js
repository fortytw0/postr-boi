
window.onload = function(){document.getElementById('loginorsignup').focus()}
document.addEventListener('keyup' , parse_login_or_signup)

function parse_login_or_signup(event) 
{

if (event.key == 'Enter')
{
    
    var selected_option = document.getElementById('loginorsignup');
    selected_option.readOnly = true

    if (selected_option.value.trim() =='login') 
    {
        console.log('entered input was login')
        continue_with_login()
    }

    else if (selected_option.value.trim() =='signup') 
    {
        console.log('entered input was signup')
        window.location.href = 'signup'
    } 

    else if (selected_option.value.trim() == '') 
    {   
        console.log('entered input was blank.')
        //pass
    }   

    else 
    {
        console.log('some random input has been given.')
        console.log(selected_option.value.trim())
    }

    
}}
function continue_with_login() 
{
    var login_ack = document.getElementsByClassName('login-ack')[0]
    var login_username = document.getElementsByClassName('login-username')[0]
    var login_password = document.getElementsByClassName('login-password')[0]
    var login_auth = document.getElementsByClassName('login-auth')[0]

    var terminal = document.getElementById('terminal')

    terminal.appendChild(login_ack)
    terminal.appendChild(login_username)

    console.log(terminal.childNodes[6])

    document.getElementById('loginorsignup').blur()
    terminal.childNodes[6].focus()
    




}
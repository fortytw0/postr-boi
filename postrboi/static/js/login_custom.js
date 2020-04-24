all_nodes = {0 : 'loginorsignup' , 1 : 'login-ack' , 2 : 'login-username' , 3 : 'login-password' ,4 : 'login-auth' , 5: 'forgot-cred'}
node_index = 0 

window.onload = focus_on(0)
document.addEventListener('keyup' , parse_action)


function focus_on() 
{
    if (node_index > 0) 
    {
        var old_node = document.getElementById(all_nodes[node_index-1]);
        old_node_input = old_node.getElementsByTagName('input')
        
        if (old_node_input.length > 0)
        {
            old_node_input[0].blur();
            old_node_input[0].readOnly = true;

        }

        
        
    }

    var current_node = document.getElementById(all_nodes[node_index]);
    current_node_input = current_node.getElementsByTagName('input');

    console.log(current_node_input)

    if (current_node_input.length > 0)
    {
        current_node_input[0].focus();
    }
    else 
    {   
        var ev = document.createEvent('Event');
        ev.initEvent('keypress')
        ev.key = 'Enter'
        parse_action(event=ev)
        console.log('simulated enter event')

    }

    

}

function parse_action (event ) 
{  
    
    var terminal = document.getElementById('terminal');

    if (event.key == 'Enter')
    {   

        node_index += 1 ;
        new_child_node = document.getElementsByClassName(all_nodes[node_index])[0];

        terminal.appendChild(new_child_node);
        focus_on()
    }

}








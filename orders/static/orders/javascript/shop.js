/*
    Copyright (C) 2019 OM SANTOSHKUMAR MASNE. All Rights Reserved.
    Licensed under the GNU Affero General Public License v3.0 only (AGPL-3.0-only) license.
    See License.txt in the project root for license information.
*/

// Maximum 10 orders are recieved upon the loading of the window.
// So, when the orders are completed, new orders are to be recieved.
// Also, the old (completed) orders are to be removed from the orders list.
// All this is done by reloading the window in every 60 seconds (1 minute).

// This is the reload timer's starting value.
var reload_time = 60;

// The startup function is executed when the DOM is loaded completely.
document.addEventListener("DOMContentLoaded", startup);

// The startup function sets the properties as per the requirements.
function startup()
{
    console.log("JAVASCRIPT STARTED!");
    get_orders();
    document.getElementById('reload-timer').innerHTML = reload_time;

    // The 'update_time' function is called every (1) second.
    setInterval(update_time, 1000);
}

// This function gets the list of the orders to be completed.
// It works as an AJAX system.
function get_orders()
{
    const request = new XMLHttpRequest();
    const data = new FormData();
    data.append('get-orders',"last_ten");
    request.open('POST', '/get-orders/');
    request.send(data);
    request.onload = () => {
        const data = request.responseText;
        if(data)
        {
            data_recieved = JSON.parse(request.responseText);
            if(data_recieved.orders_status)
            {
                order_ids = data_recieved.orders_id;
                for(var i = 0; i < order_ids.length; i++)
                {
                    const li = document.createElement('li');
                    li.setAttribute('class', 'order');
                    li.addEventListener('click', display_info);
                    li.innerHTML = order_ids[i];
                    document.getElementById('orders-list').append(li);
                }
            }
        }
        else
        {
            console.log("Request failed!");
        }
    }
    return false;
}

// This function displays the selected order's information.
// It works as an AJAX system.
function display_info(event)
{
    reset_info_box();
    selected_obj = event.target;
    document.getElementsByClassName('order-info')[0].style.display = 'block';

    const request = new XMLHttpRequest();
    const data = new FormData();
    data.append('order-id', selected_obj.innerHTML);
    request.open('POST', '/get-order-info/');
    request.send(data);
    request.onload = () => {
        const data = request.responseText;
        if(data)
        {
            data_recieved = JSON.parse(request.responseText);
            if(data_recieved.order_info_status)
            {
                document.getElementById('order-id').innerHTML = data_recieved.order_id;
                document.getElementById('order-price').innerHTML = data_recieved.price;
                if(data_recieved.order_status)
                {
                    document.getElementById('order-status').innerHTML = 'Completed!';
                }
                else
                {
                    document.getElementById('order-status').innerHTML = 'Pending';
                }

                order_contents = data_recieved.content;
                for(var i = 0; i < order_contents.length; i++)
                {
                    const li = document.createElement('li');
                    li.innerHTML = order_contents[i];
                    document.getElementById('order-content-list').append(li);
                }

                const btn = document.createElement('button');
                btn.setAttribute('class', 'btn btn-primary');
                btn.setAttribute('data-order_id', data_recieved.order_id);
                btn.addEventListener('click', complete_order);
                btn.innerHTML = 'Complete Order!';
                document.getElementById('order-complete-btn-container').append(btn);
            }
        }
    }
    return false;
}

// This functions is used to mark an order as 'Completed'.
// It works as an AJAX system.
function complete_order(event)
{
    order_id = event.target.dataset.order_id;
    const request = new XMLHttpRequest();
    const data = new FormData();
    data.append('order-id', order_id);
    request.open('POST', '/complete-order/');
    request.send(data);
    request.onload = () => {
        const data = request.responseText;
        if(data)
        {
            data_recieved = JSON.parse(request.responseText);
            if(data_recieved.order_status)
            {
                document.getElementById('order-status').innerHTML = 'Completed!';
            }
        }
    }
    return false;
}

// This function is used to reset (clear) the order information area fields.
function reset_info_box()
{
    document.getElementById('order-id').innerHTML = '';
    document.getElementById('order-price').innerHTML = '';
    document.getElementById('order-status').innerHTML = '';
    document.getElementById('order-content-list').innerHTML = '';
    document.getElementById('order-complete-btn-container').innerHTML = '';
}

// This function is used to update the reload timer's value.
// When the value of timer reaches (becomes) 0, then, the window is reloaded.
// It is called every (1) second.
function update_time()
{
    reload_time -= 1;
    document.getElementById('reload-timer').innerHTML = reload_time;
    if(reload_time === 0)
    {
        location.reload();
    }
}

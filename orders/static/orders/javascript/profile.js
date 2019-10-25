/*
    Copyright (C) 2019 OM SANTOSHKUMAR MASNE. All Rights Reserved.
    Licensed under the GNU Affero General Public License v3.0 only (AGPL-3.0-only) license.
    See License.txt in the project root for license information.
*/

// The virtual cart is an array.
// The cart items are stored in the Local Storage (browser).
// Although storing the cart items on the server side would be a great way to store items, but, for this project they are stored in the local storage.
var cart_items = [];

// The startup function is executed when the DOM is loaded completely.
document.addEventListener("DOMContentLoaded", startup);

// The startup function sets the properties as per the requirements.
function startup()
{
    console.log("JAVASCRIPT STARTED!");

    document.getElementById('btn-place-order').addEventListener('click', place_order_alert);

    document.getElementById('display-price').style.display = 'none';
    document.getElementById('price-warning').style.display = 'none';

    var cart_items_local_storage = localStorage.getItem('cart_items');
    if(cart_items_local_storage)
    {
        cart_items = JSON.parse(cart_items_local_storage);
    }

    display_cart(cart_items);

    document.getElementsByName('cart-items-get-price')[0].setAttribute('value', cart_items);
    document.getElementsByName('cart-items-place-order')[0].setAttribute('value', cart_items);

    document.getElementById('clear-cart').onclick = () => {
        localStorage.removeItem('cart_items');
        location.reload();
    }

    document.querySelector('#form-get-price').onsubmit = get_price;

}

// This function removes the selected item from the cart.
function remove_item()
{
    item_element = event.target;
    item_name = item_element.getAttribute('value');

    index_to_be_removed = cart_items.indexOf(item_name);
    if(index_to_be_removed != -1)
    {
        cart_items.splice(index_to_be_removed, 1);
        console.log("Removed from cart : " + item_name);
    }
    else
    {
        alert('Something went wrong!\nPlease reload the page.');
    }

    localStorage.setItem("cart_items", JSON.stringify(cart_items));
    document.getElementsByName('cart-items-get-price')[0].setAttribute('value', cart_items);
    document.getElementsByName('cart-items-place-order')[0].setAttribute('value', cart_items);
    display_cart(cart_items);

    document.getElementById('display-price').style.display = 'none';
    document.getElementById('price-warning').style.display = 'none';
}

// This functions displays the cart item(s) in the profile page.
function display_cart(cart_items)
{
    document.getElementById('remove-item-message').style.display = 'block';
    document.getElementById('clear-cart').style.display = 'block';
    if(cart_items.length === 0)
    {
        document.getElementById('remove-item-message').style.display = 'none';
        document.getElementById('clear-cart').style.display = 'none';
    }

    var cart_list = document.getElementById('cart-list');
    cart_list.innerHTML= "";

    for(let i = 0; i < cart_items.length; i++)
    {
        const li = document.createElement('li');
        cart_item_strings = cart_items[i].split('--');
        if(cart_item_strings[2] != 'default')
        {
            li.innerHTML = cart_item_strings[0] + " => " + cart_item_strings[1] + " => " + cart_item_strings[2];
        }
        else
        {
            li.innerHTML = cart_item_strings[0] + " => " + cart_item_strings[1];
        }
        li.setAttribute('class', "cart-list-display");
        li.addEventListener('click', remove_item);
        li.setAttribute('value', cart_items[i]);
        cart_list.append(li);
    }
}

// This function checks the price of the items that would be in the cart.
// It works as an AJAX system.
function get_price()
{
    const request = new XMLHttpRequest();
    const data = new FormData();
    data.append('cart-items-get-price', cart_items);

    request.open('POST','/get-price/');

    request.send(data);

    request.onload = () => {
        const data_recieved = JSON.parse(request.responseText);

        if(data_recieved.price_status === true)
        {
            document.getElementById('display-price').style.display = 'block';
            document.getElementById('display-price-value').innerHTML = data_recieved.price;
        }
        else
        {
            document.getElementById('price-warning').style.display = 'block';
        }

        if(data_recieved.price === '0')
        {
            document.getElementById('price-warning').style.display = 'block';
        }
    }
    return false;
}

// This function displays a confirmation window before placing the orders.
// Orders are only placed after they are confirmed by the user.
function place_order_alert()
{
    var r = confirm("Place order NOW!");
    if(r === true)
    {
        console.log('Clicked OK!');
        var order_form = document.getElementById('form-place-order');
        order_form.submit();
        return true;
    }
    else
    {
        console.log('Clicked Cancel!');
        return false;
    }
}

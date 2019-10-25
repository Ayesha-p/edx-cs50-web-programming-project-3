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
    var cart_items_local_storage = localStorage.getItem('cart_items');
    if(cart_items_local_storage)
    {
        cart_items = JSON.parse(cart_items_local_storage);
    }

    if(document.getElementById('greeting'))
    {
        user_logged = true;
    }
    else
    {
        user_logged = false;
    }

    // Following code checks for clicks (to add items to the cart).
    let cart = document.getElementsByClassName('add_to_cart');
    for(let i =0; i < cart.length; i++)
    {
        cart[i].addEventListener('click', add_to_cart);
    }
}

// This function adds the selected (clicked) items to the cart.
function add_to_cart()
{
    selected_item = event.target;
    selected_item_name = selected_item.dataset.item;
    console.log("ADDED TO CART! " + selected_item_name);

    cart_items.push(selected_item_name);

    localStorage.setItem("cart_items", JSON.stringify(cart_items));

    selected_item.innerHTML = "Added to cart!";
    selected_item.setAttribute('class', 'added_to_cart');
}

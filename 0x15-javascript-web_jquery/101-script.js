$.when($.ready).then(function () {
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });
});
$.when($.ready).then(function () {
  $('#remove_item').click(function () {
    $('.my_list li:last').remove();
  });
});
$.when($.ready).then(function () {
  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});

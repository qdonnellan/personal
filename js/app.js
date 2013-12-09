// This is a simple *viewmodel* - JavaScript that defines the data and behavior of your UI

var viewModel = {
  month: ko.observable('08'),
  html: ko.observable('no content yet'),
};

$("#thebutton").click(function () {
  $.getJSON("/api/blog/2013/07/21", function (result) {
    viewModel.month(result.month);
    viewModel.html(result.html);
  });
});

ko.applyBindings(viewModel); // This makes Knockout get to work

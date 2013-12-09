// This is a simple *viewmodel* - JavaScript that defines the data and behavior of your UI

var viewModel = {
  content: ko.observable("nothing here yet"),
  title: ko.observable("no title set yet")
};

$.getJSON('/api/blog/2013/07/21', function(data) {
   ko.mapping.fromJS(data, {}, viewModel);
});

ko.applyBindings(viewModel); // This makes Knockout get to work


// Copyright (C) 2013 Quentin Donnellan
// License: MIT (http://opensource.org/licenses/MIT)
// www.qdonnellan.com

var blogViewModel = {
  month: ko.observable(''),
  year: ko.observable(''),
  day: ko.observable(''),
  html: ko.observable('<h1 class="text-muted"><i class="fa fa-cog fa-spin"></i> loading...</h1>'),
  title: ko.observable()
};

function updateBlogViewModel(data) {
  blogViewModel.month(data.month);
  blogViewModel.html(data.html);
  blogViewModel.title(data.title);
  blogViewModel.year(data.year);
  blogViewModel.day(data.day);
  $('[data-spy="scroll"]').each(function () {
    var $spy = $(this).scrollspy('refresh')
  });
}

$.getJSON("/api/blog/latest", function (result) {
    updateBlogViewModel(result)
  });

// blog typehead stuff
$('#blog .typeahead').typeahead({                              
  name: 'blog-list',                                                      
  prefetch: '/api/blog/map',
  template: [                                                           
    '<p class="tt-blog-name">{{name}}</p>',                                      
    '<p class="tt-blog-date">{{date}}</p>'                         
  ].join(''),                                                                 
  engine: Hogan                                             
});

$('#search-input').bind('typeahead:selected', function(obj, datum, name) {      
    blog_ref = datum.reference;
    $.getJSON(blog_ref, function (result) {
      updateBlogViewModel(result)
    });
});

ko.applyBindings(blogViewModel); // This makes Knockout get to work

// smooth scrolling from one #id to another #id on the page
$(function() {
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') 
        || location.hostname == this.hostname) {

      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});

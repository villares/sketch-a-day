
Array.from(document.querySelectorAll('[id]')).forEach(e => {
   const a = document.createElement('a');
   a.href=`#${e.id}`;
   e.parentNode.replaceChild(a, e);
   a.appendChild(e);
});

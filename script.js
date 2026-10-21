/* Radhika Atolia portfolio — motion & interaction. No dependencies. */
(function(){
'use strict';
var $=function(s,c){return (c||document).querySelector(s)};
var $$=function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s))};
var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var fine=window.matchMedia('(hover:hover) and (pointer:fine)').matches;
var clamp=function(v,a,b){return Math.max(a,Math.min(b,v))};

/* shutter transition: quote stays readable for ~1.1s TOTAL across drop + load + lift --- */
var HOLD=1100; // ms the quote should be on screen overall (reading time)
var leftAt=+sessionStorage.getItem('leftAt')||0, arrived=Date.now();
try{sessionStorage.removeItem('leftAt')}catch(e){}
var sinceLeft=leftAt?arrived-leftAt:0;            // time already spent dropping + loading
function lift(){var wait=leftAt?HOLD-(Date.now()-leftAt):HOLD-(Date.now()-arrived)+0;setTimeout(function(){document.body.classList.add('ready')},Math.max(wait,60))}
if(reduce){document.body.classList.add('ready')}else if(document.readyState==='complete')lift();else window.addEventListener('load',lift);
setTimeout(function(){document.body.classList.add('ready')},3500);
window.addEventListener('pageshow',function(e){if(e.persisted)document.body.classList.add('ready')});
// prefetch pages on hover/touch so the load part is ~instant
var pf={};function prefetch(a){var u=new URL(a.href,location.href);if(u.origin!==location.origin||pf[u.href]||u.pathname===location.pathname)return;pf[u.href]=1;var l=document.createElement('link');l.rel='prefetch';l.href=u.href;document.head.appendChild(l)}
document.addEventListener('mouseover',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(a)prefetch(a)});
document.addEventListener('touchstart',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(a)prefetch(a)},{passive:true});
document.addEventListener('click',function(e){
  var a=e.target.closest&&e.target.closest('a[href]');if(!a||e.defaultPrevented||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.button)return;
  if(a.target&&a.target!=='_self'||a.hasAttribute('download')||a.hasAttribute('data-lb'))return;
  var u=new URL(a.href,location.href);if(u.origin!==location.origin)return;
  if(u.pathname===location.pathname&&u.search===location.search)return;
  if(reduce)return;
  e.preventDefault();
  var Q=window.__Q||[],qi=Math.floor(Math.random()*Q.length),c=document.querySelector('.curtain');
  if(c&&Q[qi])c.querySelector('.curtain__q').textContent=Q[qi];
  try{sessionStorage.setItem('leftAt',Date.now());sessionStorage.setItem('nq',qi)}catch(x){}
  document.body.classList.remove('ready','lock');
  setTimeout(function(){location.href=a.href},480);
});

/* split text ----------------------------------------------- */
$$('[data-split]').forEach(function(el){
  var i=0;
  (function walk(node){
    $$(':scope > *, :scope',node).length; // noop
  })(el);
  function wrap(node){
    Array.prototype.slice.call(node.childNodes).forEach(function(n){
      if(n.nodeType===3){
        var frag=document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach(function(t){
          if(!t)return;
          if(/^\s+$/.test(t)){frag.appendChild(document.createTextNode(' '));return}
          var w=document.createElement('span');w.className='w';
          var s=document.createElement('span');s.textContent=t;s.style.setProperty('--i',i++);
          w.appendChild(s);frag.appendChild(w);
        });
        node.replaceChild(frag,n);
      }else if(n.nodeType===1&&!n.querySelector('svg')&&n.tagName!=='BR'){wrap(n)}
      else if(n.nodeType===1&&n.querySelector('svg')){
        // keep decorative svg intact: wrap the text part only
        var txt=n.firstChild;if(txt&&txt.nodeType===3){var f=document.createDocumentFragment();
          var w=document.createElement('span');w.className='w';var s=document.createElement('span');s.textContent=txt.textContent;s.style.setProperty('--i',i++);w.appendChild(s);n.replaceChild(w,txt)}
      }
    });
  }
  wrap(el);el.classList.add('split');
});
/* scrub text (words light up as you scroll) --------------- */
var scrubs=$$('[data-scrub]').map(function(el){
  var words=[];
  (function wrap(node){
    Array.prototype.slice.call(node.childNodes).forEach(function(n){
      if(n.nodeType===3){
        var frag=document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach(function(t){
          if(!t)return;if(/^\s+$/.test(t)){frag.appendChild(document.createTextNode(' '));return}
          var w=document.createElement('span');w.className='w'+(node.classList&&node.classList.contains('hl')?' hi':'');w.textContent=t;words.push(w);frag.appendChild(w)});
        node.replaceChild(frag,n);
      }else if(n.nodeType===1){wrap(n)}
    });
  })(el);
  el.classList.add('scrub');return {el:el,words:words};
});

/* reveal --------------------------------------------------- */
var io=('IntersectionObserver' in window)?new IntersectionObserver(function(es){
  es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}});
},{threshold:.14,rootMargin:'0px 0px -6% 0px'}):null;
$$('[data-reveal],.split,.job').forEach(function(el){
  if(!io||reduce){el.classList.add('in')}else io.observe(el);
});
// stagger helper: children of [data-stagger]
$$('[data-stagger]').forEach(function(p){$$(':scope > *',p).forEach(function(c,i){c.setAttribute('data-reveal',c.getAttribute('data-reveal')||'up');c.style.setProperty('--i',i);if(io&&!reduce)io.observe(c);else c.classList.add('in')})});

/* counters ------------------------------------------------- */
var cio=('IntersectionObserver' in window)?new IntersectionObserver(function(es){es.forEach(function(e){
  if(!e.isIntersecting)return;cio.unobserve(e.target);
  var el=e.target,end=parseFloat(el.dataset.count),dec=(el.dataset.count.split('.')[1]||'').length,suf=el.dataset.suffix||'',t0=null;
  if(reduce){el.textContent=end.toFixed(dec)+suf;return}
  (function step(t){if(!t0)t0=t;var p=clamp((t-t0)/1400,0,1),v=end*(1-Math.pow(1-p,4));el.textContent=v.toFixed(dec)+suf;if(p<1)requestAnimationFrame(step)})(performance.now());
})},{threshold:.5}):null;
$$('[data-count]').forEach(function(el){if(cio)cio.observe(el);else el.textContent=el.dataset.count+(el.dataset.suffix||'')});

/* nav ------------------------------------------------------ */
var nav=$('.nav'),tog=$('.nav__toggle'),bar=$('.progress i');
if(tog)tog.addEventListener('click',function(){var o=nav.classList.toggle('open');tog.textContent=o?'✕':'☰';document.body.classList.toggle('lock',o)});
$$('.nav__links a').forEach(function(a){a.addEventListener('click',function(){nav.classList.remove('open');document.body.classList.remove('lock');if(tog)tog.textContent='☰'})});

/* magnetic buttons + tilt ---------------------------------- */
if(fine&&!reduce){
  /* no magnetic drift on .btn: the button system's hover state is the hard
     offset shadow, and an inline transform would slide the pill off it. */
  $$('[data-tilt]').forEach(function(el){
    var max=parseFloat(el.dataset.tilt)||8,tgt=el.querySelector('[data-tilt-in]')||el;
    el.addEventListener('mousemove',function(e){var r=el.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;
      tgt.style.transform='rotateY('+(x*max*2)+'deg) rotateX('+(-y*max*2)+'deg) translateZ(0)'});
    el.addEventListener('mouseleave',function(){tgt.style.transform=''});
  });
  $$('.float3d').forEach(function(el){
    var im=$('img',el);if(!im)return;
    el.addEventListener('mousemove',function(e){var r=el.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;im.style.transform='perspective(900px) rotateY('+(x*16)+'deg) rotateX('+(-y*12)+'deg) translateZ(20px)'});
    el.addEventListener('mouseleave',function(){im.style.transform=''});
  });
}

/* hero 3D stage -------------------------------------------- */
var stage=$('.stage');
if(stage){
  var inn=$('.stage__in',stage),layers=$$('.layer',stage).concat($$('.chip3d',stage));
  var base=layers.map(function(l){return l.style.getPropertyValue('--z')||''});
  var tx=0,ty=0,cx=0,cy=0,raf=null;
  function loop(){cx+=(tx-cx)*.08;cy+=(ty-cy)*.08;
    inn.style.transform='rotateY('+(cx*14)+'deg) rotateX('+(-cy*12)+'deg)';
    layers.forEach(function(l){var z=parseFloat(l.dataset.depth||0);if(!z)return;l.style.translate=(cx*z*-.22)+'px '+(cy*z*-.22)+'px'});
    if(Math.abs(tx-cx)>.001||Math.abs(ty-cy)>.001)raf=requestAnimationFrame(loop);else raf=null}
  var move=function(x,y){tx=x;ty=y;if(!raf)raf=requestAnimationFrame(loop)};
  if(!reduce){
    var hero=$('.hero');
    hero.addEventListener('mousemove',function(e){var r=stage.getBoundingClientRect();move(clamp((e.clientX-r.left)/r.width-.5,-.9,.9),clamp((e.clientY-r.top)/r.height-.5,-.9,.9))});
    hero.addEventListener('mouseleave',function(){move(0,0)});
    window.addEventListener('deviceorientation',function(e){if(e.gamma==null)return;move(clamp(e.gamma/35,-.8,.8),clamp((e.beta-45)/35,-.8,.8))});
  }
}

/* scroll-driven ---------------------------------------------- */
var par=$$('[data-speed]'),stack=$$('.scard'),hs=$$('.hscroll'),tl=$$('.tl'),toc=$$('.toc__list a, .tocbar a'),secs=toc.map(function(a){return $(a.getAttribute('href'))}),covers=$$('.cs-cover__in'),csb=$('.cs-body'),tocEl=$('.toc'),totop=$('.totop'),tbar=$('.tocbar');
var ticking=false,lastY=0,lastCur=-2;
function frame(){
  ticking=false;var y=window.scrollY,vh=window.innerHeight,dh=document.documentElement.scrollHeight-vh;
  if(bar)bar.style.transform='scaleX('+clamp(y/dh,0,1)+')';
  if(nav&&!nav.classList.contains('open')){nav.classList.toggle('hide',y>420&&y>lastY+2);if(y<lastY-2)nav.classList.remove('hide')}
  lastY=y;
  if(!reduce){
    par.forEach(function(el){var r=el.getBoundingClientRect();if(r.bottom<-200||r.top>vh+200)return;var s=parseFloat(el.dataset.speed),c=(r.top+r.height/2-vh/2);el.style.translate='0 '+(c*s*-1)+'px'});
    scrubs.forEach(function(s){var r=s.el.getBoundingClientRect(),p=clamp((vh*.85-r.top)/(r.height+vh*.35),0,1),n=Math.round(p*s.words.length);s.words.forEach(function(w,i){w.classList.toggle('on',i<n)})});
    if(window.innerWidth>860)stack.forEach(function(c,i){
      var nx=stack[i+1];if(!nx){c.style.transform='';return}
      var r=nx.getBoundingClientRect(),top=parseFloat(getComputedStyle(nx).top)||0,p=clamp(1-(r.top-top)/(vh*.8),0,1);
      c.style.transform='scale('+(1-p*.06)+') translateY('+(-p*10)+'px)';c.style.filter='brightness('+(1-p*.12)+')';
    });
    hs.forEach(function(h){
      if(window.innerWidth<=800)return;
      var tr=$('.hscroll__track',h),r=h.getBoundingClientRect(),total=r.height-vh,p=clamp(-r.top/total,0,1),dist=tr.scrollWidth-window.innerWidth+60;
      tr.style.transform='translate3d('+(-dist*p)+'px,0,0)';
    });
    covers.forEach(function(c){var r=c.getBoundingClientRect();var p=clamp((vh-r.top)/(vh+r.height),0,1);c.parentNode.style.setProperty('--p',p)});
  }
  tl.forEach(function(t){var r=t.getBoundingClientRect(),p=clamp((vh*.7-r.top)/r.height,0,1);t.style.setProperty('--p',p)});
  if(secs.length){var cur=-1,n=secs.length/2;secs.forEach(function(s,i){if(s&&s.getBoundingClientRect().top<vh*.4)cur=i%n});toc.forEach(function(a,i){var on=cur>=0&&(i%n)===cur;a.classList.toggle('on',on);if(on&&tbar&&a.parentNode===tbar&&lastCur!==cur){var l=a.offsetLeft-tbar.clientWidth/2+a.offsetWidth/2;tbar.scrollTo({left:l,behavior:'smooth'})}})}
  if(csb&&tocEl){var br=csb.getBoundingClientRect();tocEl.style.setProperty('--tp',clamp((vh*.4-br.top)/Math.max(1,br.height-vh*.2),0,1))}
  lastCur=cur;
  if(totop)totop.classList.toggle('show',y>900)
}
function req(){if(!ticking){ticking=true;requestAnimationFrame(frame)}}
window.addEventListener('scroll',req,{passive:true});window.addEventListener('resize',req);frame();

/* filters ---------------------------------------------------- */
var fb=$$('.filters button');
fb.forEach(function(b){b.addEventListener('click',function(){
  fb.forEach(function(x){x.classList.remove('on')});b.classList.add('on');var f=b.dataset.f;
  $$('.pcard').forEach(function(c){var show=f==='all'||(c.dataset.cat||'').split(' ').indexOf(f)>-1;c.classList.toggle('hide',!show);if(show){c.style.opacity=0;c.style.transform='translateY(20px)';requestAnimationFrame(function(){requestAnimationFrame(function(){c.style.opacity=1;c.style.transform=''})})}});
  req();
})});

/* lightbox ---------------------------------------------------- */
var items=$$('a[data-lb]');
if(items.length){
  var lb=document.createElement('div');lb.className='lb';lb.setAttribute('role','dialog');lb.setAttribute('aria-modal','true');
  lb.innerHTML='<div class="lb__scroller"><img alt=""></div><span class="ct"></span><button class="x" aria-label="Close">✕</button><button class="pv" aria-label="Previous">←</button><button class="nx" aria-label="Next">→</button>';
  document.body.appendChild(lb);
  var im=$('img',lb),ct=$('.ct',lb),sc=$('.lb__scroller',lb),grp=[],idx=0;
  function show(i){idx=(i+grp.length)%grp.length;var a=grp[idx];im.src=a.href;im.alt=($('img',a)||{}).alt||'';ct.textContent=(idx+1)+' / '+grp.length;sc.scrollTop=0;$('.pv',lb).style.display=$('.nx',lb).style.display=grp.length>1?'':'none'}
  function open(a){grp=items.filter(function(x){return x.dataset.lb===a.dataset.lb});show(grp.indexOf(a));lb.classList.add('open');requestAnimationFrame(function(){lb.classList.add('show')});document.body.classList.add('lock')}
  function close(){lb.classList.remove('show');document.body.classList.remove('lock');setTimeout(function(){lb.classList.remove('open');im.src=''},350)}
  items.forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();open(a)})});
  $('.x',lb).onclick=close;$('.pv',lb).onclick=function(){show(idx-1)};$('.nx',lb).onclick=function(){show(idx+1)};
  sc.addEventListener('click',function(e){if(e.target===sc)close()});
  document.addEventListener('keydown',function(e){if(!lb.classList.contains('open'))return;if(e.key==='Escape')close();if(e.key==='ArrowLeft')show(idx-1);if(e.key==='ArrowRight')show(idx+1)});
}

if(totop)totop.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'})});
/* rotating hero line ----------------------------------------------- */
$$('.rot').forEach(function(el){var w=el.dataset.words.split('|'),i=0,txt='',del=false;
  if(reduce){el.textContent=w[0];return}
  (function tick(){var full=w[i];txt=del?full.slice(0,txt.length-1):full.slice(0,txt.length+1);el.textContent=txt;var d=del?22:48;
    if(!del&&txt===full){del=true;d=1700}else if(del&&txt===''){del=false;i=(i+1)%w.length;d=300}setTimeout(tick,d)})();
});
/* hire widget + copy email ------------------------------------------ */
var hire=$('.hire'),toast=$('.toast'),tt;
function say(m){
  if(!toast){toast=document.createElement('div');toast.className='toast';toast.setAttribute('role','status');document.body.appendChild(toast)}
  toast.textContent=m;toast.classList.add('show');clearTimeout(tt);tt=setTimeout(function(){toast.classList.remove('show')},2600)}
/* footer copy-email. Lives here so every page shares one implementation, and
   so the icon is left intact (setting textContent would delete the svg). */
$$('.email-copy').forEach(function(b){
  var mail=(($('.email-text',b.parentNode)||{}).textContent||'').trim()||'radhikaselement@gmail.com';
  b.addEventListener('click',function(){
    (navigator.clipboard?navigator.clipboard.writeText(mail):Promise.reject())
      .then(function(){say('Copied '+mail)},function(){location.href='mailto:'+mail})});
});
if(hire){$('.hire__b',hire).addEventListener('click',function(e){e.stopPropagation();var o=hire.classList.toggle('open');this.setAttribute('aria-expanded',o)});
  document.addEventListener('click',function(e){if(!hire.contains(e.target))hire.classList.remove('open')});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')hire.classList.remove('open')});
  $$('.copy',hire).forEach(function(b){b.addEventListener('click',function(){var t=b.dataset.copy;
    (navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){say('Copied ✓ Now go write something nice 😌')},function(){location.href='mailto:'+t})})})}
var yr=$('#yr');if(yr)yr.textContent=new Date().getFullYear();
})();

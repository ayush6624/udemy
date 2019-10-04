# Web Dev CheatSheet

## Starting a project

npm init
vs code live server
cloudflared tunnel --url localhost:5500

## Starting a Doc

Just type `!` and Enter
For Dummy para type lorem and tab for specific words type lorem10
alt + line up/down
ctrl+shift +updown for multiple line edditing
holding alt and then clicking randomly for multiple line editing
type some thing like (h1*3) and it will do it 3 times
just type p and tab and autmatiicaly same for `a`
if you want to edit multiple pbject names select it press ctrl d and boom!
use `#header` to make a div of if header
div is a block level element
span is an inline element
convert by display: inline/block
gen use div id rather than classes, no same id on the page
classes can have attributes which can be repeated on the same page
use &copy, &yen, &gt etc for special chars
for stylesheet type link below the meta tags
`#` is for id and `.` is for classes
you can assign both id and classes to divs
for something like green-text use classes as they are reusable
span in the text/anywhere so we can refer in the nested css like #about-me p h2 span{ property}

for css:
    Background: url(./img/abc.png) no-repeat(for not repating due to size of div) `center center/cover` for position and cover property to be acitvated
    background-attachment to fixed 
    height, width(for div)
    color: for text

    padding: top right bottom left or padding: (top&bottom) (left&right)
    same for margin
    eg- padding: 20 20 10 20 (clockwise top right bottom left)or padding: 20 10
    defualt: 16px >> 1em compared to multiplying so 2em is 32px

    border: 2px #eeeeee solid/dashed
    you can have border radius (also can specify top left,etc)


you can wrap divs in a main div say container class
assign container class for max-width: 500px (say)(max width for mobile)
you can also align it to the middle by margin: 30px auto (top/bottom left/right)

font-family
line-height: 1.2rem;

for Links 
we can use like a:hover{ color, text-**} or a:visited (pseudo) or use  a class so .btn:hover{}
use margin-top/bootom/padding top/left
for text aligning - use align center
use color prop directly for text color
use bg-color for bg 
use !important flag to over-ride and make it imp

when using box, use box-sizing: border box to avoid adding padding to the width
use * {} for global props

MARGIN OUTSIDE PADDING INSIDE

for unordered list
to remove bullets use list-style: none;
u can use : li{} directly same for a{} (href)

transform -50% -50% for transforming

import streamlit as st
import streamlit.components.v1 as components


st.components.html("""
                   <link href="https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css" rel="stylesheet">
                   <link rel="stylesheet" href="style.css">
                   <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"
        integrity="sha512-16esztaSRplJROstbIIdwX3N97V1+pZvV33ABoG1H2OyTttBxEGkTsoIVsiP1iaTtM8b3+hu2kB6pQ4Clr5yug=="
        crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"
        integrity="sha512-Ic9xkERjyZ1xgJ5svx3y0u3xrvfT/uPkV99LBwe68xjy/mGtO+4eURHZBW2xW4SZbFrF1Tf090XqB+EVgXnVjw=="
        crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="script.js"></script>
    <div id="nav">
        <img src="https://eiwgew27fhz.exactdn.com/wp-content/uploads/2023/02/logo-white.svg" alt="">
        <h4>TOPTRACER RANGE</h4>
        <h4>GOLF LESSONS</h4>
        <h4>ADVENTURE GOLF</h4>
        <h4>CAFE</h4>
        <h4>EVENT</h4>
    </div>
    <div id="cursor"></div>
    <div id="cursor-blur"></div>
    <video autoplay loop muted src="https://sidcupfamilygolf.com/wp-content/uploads/2023/02/hero.mp4"></video>
    <div id="main">
        <div id="page1">
            <h1>EAT. DRINK. PLAY.</h1>
            <h2>WELCOME TO SIDCUP FAMILY GOLF!</h2>
            <p>
                Sidcup Family Golf is a multipurpose golf facility located in Sidcup,
                South East London. Passionate about technology, player development and
                making golf fun and accessible to everyone.
            </p>
            <div id="arrow">
                <i class="ri-arrow-down-line"></i>
            </div>
        </div>
        <div id="page2">
            <div id="scroller">
                <div id="scroller-in">
                    <h4>TOPTRACER RANGE</h4>
                    <h4>GOLF LESSONS</h4>
                    <h4>ADVENTURE GOLF</h4>
                    <h4>COFFEE SHOP</h4>
                    <h4>LEAGUES</h4>
                </div>
                <div id="scroller-in">
                    <h4>TOPTRACER RANGE</h4>
                    <h4>GOLF LESSONS</h4>
                    <h4>ADVENTURE GOLF</h4>
                    <h4>COFFEE SHOP</h4>
                    <h4>LEAGUES</h4>
                </div>
            </div>
            <div id="about-us">
                <img src="https://eiwgew27fhz.exactdn.com/wp-content/uploads/2023/02/home-about-1-300x200.jpg?strip=all&lossy=1&sharp=1&ssl=1"
                    alt="">
                <div id="about-us-in">
                    <h3>About-US</h3>
                    <p>Home to a 46-bay, multi-tier, floodlit driving range, powered by Toptracer Range technology.
                        Complimented by a practice green and bunker, coffee shop and American Golf Store. There truly is
                        something for everyone as we also boast two outdoor 18-hole dinosaur themed crazy golf courses.
                    </p>
                </div>
                <img src="https://eiwgew27fhz.exactdn.com/wp-content/uploads/2023/02/home-about-2-300x200.jpg?strip=all&lossy=1&sharp=1&ssl=1"
                    alt="">
            </div>
            <div id="cards-container">
                <div class="card" id="card1">
                    <div class="overlay">
                        <h4>Top Racer Range</h4>
                        <p>
                            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nulla
                            quam molestias magni cupiditate architecto et enim quas facere
                            ipsum tempora?
                        </p>
                    </div>
                </div>
                <div class="card" id="card2">
                    <div class="overlay">
                        <h4>Adventure Golf</h4>
                        <p>
                            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nulla
                            quam molestias magni cupiditate architecto et enim quas facere
                            ipsum tempora?
                        </p>
                    </div>
                </div>
                <div class="card" id="card3">
                    <div class="overlay">
                        <h4>Golf Lessons</h4>
                        <p>
                            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nulla
                            quam molestias magni cupiditate architecto et enim quas facere
                            ipsum tempora?
                        </p>
                    </div>

                </div>
            </div>
            <div id="green-div">
                <img src="https://eiwgew27fhz.exactdn.com/wp-content/themes/puttosaurus/img/dots-side.svg" alt="">
                <h4>SIGN UP FOR SIDCUP NEWS AND SPECIAL OFFERS
                    STRAIGHT TO YOUR INBOX</h4>
                <img src="https://eiwgew27fhz.exactdn.com/wp-content/themes/puttosaurus/img/dots-side.svg" alt="" />
            </div>
            <div id="page3">
                <P>Excellent couple of hours, relax and enjoy in the fun. Staff were
                    accommodating, friendly and very helpful. Café on site for
                    refreshments etc. Will keep children enterntained during the holidays.
                    Worth a visit if you haven’t been.</P>
                <img id="colon1" src="https://eiwgew27fhz.exactdn.com/wp-content/themes/puttosaurus/img/quote-left.svg"
                    alt="">
                <img id="colon2" src="https://eiwgew27fhz.exactdn.com/wp-content/themes/puttosaurus/img/quote-right.svg"
                    alt="">
            </div>
            <div id="page4">
                <h1>WHAT ARE YOU WAITING FOR?</h1>
                <div class="elem">
                    <h2>TOPTRACER RANGE</h2>
                    <img src="https://eiwgew27fhz.exactdn.com/wp-content/uploads/2023/02/page-toptracer-1024x683.jpg?strip=all&lossy=1&sharp=1&ssl=1"
                        alt="" />
                </div>
                <div class="elem">
                    <h2>Golf Lessons</h2>
                    <img src="https://eiwgew27fhz.exactdn.com/wp-content/uploads/2023/02/page-lessons-1024x683.jpg?strip=all&lossy=1&sharp=1&ssl=1"
                        alt="" />
                </div>
                <div class="elem">
                    <h2>Adventure Golf</h2>
                    <img src="https://eiwgew27fhz.exactdn.com/wp-content/uploads/2023/02/page-ag-1024x682.jpg?strip=all&lossy=1&sharp=1&ssl=1"
                        alt="" />
                </div>
            </div>
            <div id="footer">
                <img src="https://eiwgew27fhz.exactdn.com/wp-content/themes/puttosaurus/img/dots-footer.svg" alt="" />
                <div id="f1">
                    <img src="https://eiwgew27fhz.exactdn.com/wp-content/uploads/2023/02/logo-white.svg" alt="" />
                </div>
                <div id="f2">
                    <h3>TOPTRACER Ranges</h3>
                    <h3>Golf Lessons</h3>
                    <h3>Adventure Golf</h3>
                </div>
                <div id="f3">
                    <h3>coffee shop</h3>
                    <h3>LEAGUES</h3>
                    <h3>Contact us</h3>
                </div>
                <div id="f4">
                    <h4>
                        A20, SIDCUP BYPASS <br />
                        CHISLEHURST <br />
                        KENT <br />
                        BR7 6RP <br />
                        TEL: 0208 309 0181 <br />
                        GET DIRECTIONS <br />
                    </h4>
                </div>
            </div>
        </div>
    </div>
    """, width=None, height=None, scrolling=False)
# st.title("Hello Techeie !!!")
# name = st.text_input("Enter your Name : ")
# fname = st.text_input("Enter Your surname: ")
# adr = st.text_area("Address: ")
# status = st.radio("Select Gender: ", ('Male', 'Female'))
# if (status == 'Male'):
#     st.success("Male")
# else:
#     st.success("Female")
# classdata = st.selectbox("Skills : ",["Software", "Hardware", "HTML", "CSS", "JavaScript", "Java", "Mobile"])

# button = st.button("Done")
# if button :
#     st.markdown(f"""
#                 Name : {name}
#                 Surname : {fname}
#                 address : {adr}
#                 class : {classdata}""")

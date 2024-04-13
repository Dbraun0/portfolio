# Imports
import streamlit as st
from streamlit_echarts import st_echarts
import requests
import json

# Functions  
@st.cache_data  
def get_image_content(url:str):
    return requests.get(url).content

get_drive_image = lambda x: get_image_content(f'https://drive.google.com/uc?id={x}')
def list_to_spec(input:list) -> list:            
    output = [
        {
            'name': level1_name,
            'children': [
                {
                    'name': level2_name,
                    'children': [
                        {
                            'name': level3_name,
                            'value': 1
                        } for level3_name in level3_list
                    ]
                } for level2_name, level3_list in level2_list.items()
            ]
        } for level1_name, level2_list in input.items()
    ]
    
    return output

def get_skills() -> dict: 
    with open('skills.json', 'r') as f: 
        return list_to_spec(json.load(f))

# Setup
skills = get_skills()
option = {
    'series': {
        'type': 'sunburst',
        'data': skills,
        'itemStyle': {
            'borderRadius': 7,
            'borderWidth': 2
            },
        'levels': [
            {},
            {
                "r0": "10%",
                "r": "30%",
                "itemStyle": {"borderWidth": 2},
                "label": {"rotate": "tangential"},
            },
            {"r0": "30%", "r": "65%", "label": {"align": "right"}},
            {
                "r0": "65%",
                "r": "67%",
                "label": {
                    'position': 'outside',
                    'padding': 3,
                    'silent': False
                    },
                "itemStyle": {"borderWidth": 3},
            },
        ]
    }
}

# App
st.image(requests.get('https://media.licdn.com/dms/image/C4E03AQEVT2v7J583CQ/profile-displayphoto-shrink_200_200/0/1539963072592?e=1718236800&v=beta&t=0nhQvmQFGCbiujJHqFvdleVIo-3j-B0tjhuhUu6vBq8').content)
st.title('Dagen Braun')
st.markdown('---')
with st.expander('Links', expanded=False): 
    st.markdown(
        '''
        - [Github](https://github.com/Dbraun0/)
        - [LinkedIn](https://www.linkedin.com/in/dagenbraun)
        - [braundagen@gmail.com](mailto:braundagen@gmail.com)
        '''
    )
summary, work_history, education, publications, certifications, personal_projects = st.tabs(['Summary', 'Work History', 'Education', 'Publications', 'Certifications', 'Personal Projects'])
with summary:
    st.markdown(
        '''
        Hello!
        
        I am a Machine Learning Engineer at Lockheed Martin Space in Sunnyvale, CA.
        
        My work currently consists of researching ML techniques for solving difficult activity-based sensemaking problems in the realm of overhead satellite imagery.
        
        
        '''
    )
    
    st.markdown('### Skills')
    st_echarts(option, height='700px')
        
with work_history: 
    with st.expander('Lockheed Martin Space - Sunnyvale, CA', expanded=True): 
        st.markdown(
            '''
            ### Senior A AI/ML Engineer
            *October 2023 - Present*
            
            Conducting computer vision-based machine learning research and development  as part of the Algorithms, Processing, and Simulations (APS) team in the Optical Payload Center of Excellence (OPCoE). 
            
            Built and trained an airplane segmentation model for overhead imagery robust to differing spatial resolutions and image sources.
            
            Created multitask classification models to simultaneously classify multiple airplane attributes for both continuous and discrete attributes.
            
            Published a paper on utilizing biologically inspired image augmentation to increase model robustness to adversarial attacks in satellite imagery.
            
            Maintaining NVIDIA-CUDA based docker image registry across the team for our ML research and development.

            
            ### A AI/ML Engineer
            *March 2023 - October 2023*
            
            ### Guidance, Navigation, and Control Engineer
            *November 2021 - March 2023*
            '''
        )
        
    with st.expander('Gurley Precision Instruments - Troy, NY', expanded=False): 
        st.markdown(
            '''
            ### Mechanical Engineer
            *May 2021 - November 2021*
            
            Designed and drafted high precision aerospace encoder components and special testing equipment for use in the Raytheon EWS and OPIR programs, as well as multiple other space programs.  Experimented with novel disc-hub bonding techniques using microsphere doped epoxy, reducing the likelihood of delamination under thermal cycling. Designed a double direct drive fixture for operation in a thermal vacuum chamber with an externally mounted motor. Began as an intern, and was promoted while completing a masters degree. 
            
            ### Mechanical Engineering Intern
            *May 2019 - May 2021*
            '''
        )
        
    with st.expander('Rensselaer Polytechnic Institute - Troy, NY', expanded=False): 
        st.markdown(
            '''
            ### Undergraduate Student Researcher
            *May 2019 - November 2021*
            
            Presented and participated in student/teacher workshops designed to promote the teaching of Generative STEM education and ethnocomputing, most notably at the Summer Educator Academy, sponsored by the American Federation of Teachers. The lesson plans were then adopted by a multitude of teachers for the teaching of programming and mathematics and their ties to culture.
            
            Designed and tested a water boiling system utilizing solar thermal tubes for ink makers in Ghana, Africa. The use of solar power reduces the physical impact of wood fire methods that negatively impact the health of artisanal ink-makers. 

            '''
        )
        
    with st.expander('OceanView at Falmouth - Falmouth, ME', expanded=False): 
        st.markdown(
            '''
            ### Server
            *May 2019 - November 2021*
            '''
        )
        
    with st.expander('Aquaboggan Waterpark - Saco, ME', expanded=False): 
        st.markdown(
            '''
            ### Slide Attendant / Maintenance Supervisor
            *May 2019 - November 2021*
            '''
        )
        
with education: 
    with st.expander('Rensselaer Polytechnic Institute - Troy, NY', expanded=True): 
        st.markdown(
            '''
            
            ### Master of Engineering
            *Aeronautical Engineering - Space Focus*
            
            Studied at Rensselaer Polytechnic Institute completing a M.E. in Aeronautical Engineering, with a focus on space systems. Graduate coursework included Numerical Design Optimization, with a final project consisting of programming a Deep Neural Network from scratch using Python, as well as a host of control systems classes leading to the implementation of a LQR controller to stabilize a model segway. The culmination of the M.E. degree consisted of developing a performance index and cost function for the selection and removal of space debris from orbit using cubesats and two-line Element sets.
            
            ### Bachelor of Science
            *Aeronautical Engineering - Space Focus*
            '''
        )
        
    with st.expander('North Yarmouth Academy - Yarmouth, ME', expanded=False): 
        st.markdown(
            '''
            ### High School
            '''
        )
        
with publications: 
    st.markdown(
        '''
        [Achieving Adversarial Robustness in Deep Learning-Based Overhead Imaging](https://ieeexplore.ieee.org/document/10092213)
        
        [Video](https://drive.google.com/file/d/10G4t9vx0V1qpmAM80OY3AA40haM9ysg8/view?usp=sharing)
        
        D. Braun, M. Reisman, L. Dewell, A. Banburski-Fahey, A. Deza and T. Poggio, "Achieving Adversarial Robustness in Deep Learning-Based Overhead Imaging," 2022 IEEE Applied Imagery Pattern Recognition Workshop (AIPR), DC, USA, 2022, pp. 1-7, doi: 10.1109/AIPR57179.2022.10092213. 
        
        keywords: {Target recognition;Biological system modeling;Perturbation methods;Surveillance;Pipelines;Neural networks;Object detection;adversarial attacks;deep learning;automatic target recognition;satellite imaging;biological learning},


        '''
    )
    st.markdown('---')
    st.markdown('[Four Cool Artificial Intelligence Technologies Article](https://www.lockheedmartin.com/en-us/news/features/2022/four-cool-artificial-intelligence-technologies.html)')
    
with certifications: 
    st.markdown(
        '''
        - Mission Solutions AI/ML Upskilling (DOD Certification)
        
        - STK Level 1
        '''
    )
    
with personal_projects: 
    with st.expander('Bluetooth Controlled Automated Plant Drip System'): 
        st.markdown(
            '''
            Initial design allowed for automated watering of 10 plants at a time, with adjustable watering frequency and duration, along with a toggle switch. 
            
            Subsequent updates replaced the ATTINY85 microcontroller with an ESP32C3 equipped with bluetooth, and a phone app that allowed for finer adjustments, as well as adding a second bin to increase the plant capacity to 20.
            '''
        )
        
        st.image(get_image_content('https://lh4.googleusercontent.com/mvpQBRABRD3z7Cr2CJJwVoHj32p2XMNcNw7R2OVRGcqdseEtU7M_A6jDZ9FRqQsfRaXnLdmNreh-YyPgCpe5XzfAllpPBS88uvxu-Nz-XIPm2htIAaIiq4_06DgBCRPjFZdEbL4h5ubagrbLmuTSsQLuFg=s2048'))
        st.image(get_image_content('https://lh3.googleusercontent.com/QiIobOJDb7HLu6Z-klg-sPBpZB53zxBDHvYEBO59tAh2d58KSsyAWHPIbM2jU1FE5HazVk6sETiTEosZsnl87iJnX97bpn2TKn0gSJyBHcey_6xtFwJIJRl1l6nl8En6aZFZhJRbAp5AuPRxonDq4rWTZg=s2048'))
        st.image(get_image_content('https://lh5.googleusercontent.com/G_MYtXhx9bwAHOeI-0EJDp7Mut-vVGWT6P574oO_VTXWiW-o1AHbI-K6NKXjXkA9ecPZQtUgVbJWivOXTQDr-h4ZnmJaxgl8z6PxksUg5r9Hg9i7iqcYbfIXl6oECsSIWcVKBj1_7b5g-Vnq-ogo3XXFfg=s2048'))

    with st.expander('Model Segway with LQR Control'): 
        st.markdown(
            '''
            [Video](https://drive.google.com/file/d/1pi3anB5ujiyDrZPVJe7-nRawB7ymoRW8/view?usp=sharing)
            
            Completed for a graduate level controls project, this model segway was stabilized using a Linear Quadratic Regulator control system tuned to give optimal control. 
            '''
        )
        
    with st.expander('Cat Counter Denial System'): 
        st.markdown(
            '''
            [Video](https://drive.google.com/file/d/1FzmjB0QcEQn9Fmf0V19I86IMNOzwVG2n/view?usp=sharing)
            
            Designed to keep my cat off of the counter, this system features two toggleable motion sensors to detect whether there is motion on the counter surface (bottom). If there is, a swinging arm will pass over the counter to scare off the cat.
            
            If motion is detected from the secondary motion detector (front facing), the system will assume a human being is working on the counter and prevent actuation of the swinging arm
            '''
        )
        
        st.image(get_drive_image('1nKybrw0ELbOyIv48dw8uZJu71Je8LJ1Q'))
        
    with st.expander('Streamlit Dashboard'): 
        st.markdown(
            '''
            You're looking at it!
            
            Also set up a locally hosted dashboard with calculators and monitoring widgets for personal use
            '''
        )
        
    with st.expander('Terrarium Lamp'): 
        st.markdown(
            '''
            Small little project to provide light to a terrarium on a day/night cycle to remove the need for outside light sources. 
            '''
        )
        
        st.image(get_drive_image('1sH3QJdS_zxa-I5D6j4qMk95V_QimBwL3'))
        st.image(get_drive_image('1sEg1c6ydu2bi88HIAt2s86nUsrcqaRzd'))
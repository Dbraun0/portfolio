# Imports
import streamlit as st

# Functions

# Setup

# App
st.image('images/headshot.jpg')
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
summary, work_history, education, publications, personal_projects = st.tabs(['Summary', 'Work History', 'Education', 'Publications', 'Personal Projects'])
with summary:
    st.markdown(
        '''
        Hi There!
        
        I am a Machine Learning Engineer at Lockheed Martin Space in Sunnyvale, CA.
        
        My work currently consists of researching ML techniques for solving difficult activity-based sensemaking problems in the realm of overhead satellite imagery.
        
        
        '''
    )
    
    st.markdown('### Skills')
    col1, col2 = st.columns(2)
    cont1, cont2 = col1.container(border=True), col2.container(border=True)
    
    with cont1: 
        st.markdown(
            '''
            - Machine Learning
            - Deep Learning
            - Data Science
            - Numerical Optimization
            - Control Theory
            '''
        )
        
    with cont2: 
        st.markdown(
            '''
            - Docker
            - Python
            - Tensorflow
            - Pytorch
            - Linux
            - Kubernetes
            - AWS
            '''
        )
        
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
            *May 2019 - November 2021*
            '''
        )
        
    with st.expander('Rensselaer Polytechnic Institute - Troy, NY', expanded=False): 
        st.markdown(
            '''
            ### Undergraduate Student Researcher
            *May 2019 - November 2021*
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
        [Acheiving Adversarial Robustness in Deep Learning-Based Overhead Imaging](https://ieeexplore.ieee.org/document/10092213)
        
        D. Braun, M. Reisman, L. Dewell, A. Banburski-Fahey, A. Deza and T. Poggio, "Achieving Adversarial Robustness in Deep Learning-Based Overhead Imaging," 2022 IEEE Applied Imagery Pattern Recognition Workshop (AIPR), DC, USA, 2022, pp. 1-7, doi: 10.1109/AIPR57179.2022.10092213. 
        
        keywords: {Target recognition;Biological system modeling;Perturbation methods;Surveillance;Pipelines;Neural networks;Object detection;adversarial attacks;deep learning;automatic target recognition;satellite imaging;biological learning},


        '''
    )
    
with personal_projects: 
    with st.expander('Bluetooth Controlled Automated Plant Drip System'): 
        st.markdown(
            '''
            WIP
            '''
        )
        
    with st.expander('Model Segway with LQR Control'): 
        st.markdown(
            '''
            WIP
            '''
        )
        
    with st.expander('Cat Counter Denial System'): 
        st.markdown(
            '''
            WIP
            '''
        )
        
    with st.expander('Streamlit Dashboard'): 
        st.markdown(
            '''
            WIP
            '''
        )
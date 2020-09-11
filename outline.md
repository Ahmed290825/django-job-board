Job:
    - title
    - location 
    - type
    - description
    - published at 
    - vacancy
    - salary 
    - category
    - experience
    - gender
    - apply
    - post job
    
Blog:
    - title
    - description
    - created at 
    - category
    - tags
    - author 
    - search
    - comment
    - recent posts
    
   
contact 
home


URL : Path
VIEW : Logic
MODELS : DB
DB 
MODELS : DB
TEMPLATES : frontend

Relations:
    - one to many [user posts]  Foreignkey
    - many to many [users groups] 
    - one to one [user account]  
    
       
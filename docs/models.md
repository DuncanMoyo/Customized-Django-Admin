###MODEL ARCHITECTURE PLANNING****

Membership
    - slug
    - type (free, ent, pro)
    - price
    - stripe plan id

UserMembership
    - User                      (foreignkey to default user)
    - stripe customer id
    - membership type           (foreignkey to Membership)
    
Subscription
    - user membership           (foreignkey to User membership)
    - stripe subscription id    
    - active

Course
    - slug
    - title
    - description
    - allowed memberships       (ManytoManyField to Membership)

Lesson
    - slug
    - title
    - course                    (foreignkey to Course)
    - position
    - video
    - thumbnail
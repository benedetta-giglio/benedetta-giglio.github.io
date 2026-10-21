---
layout: post
title: "The physics behind balancing on hands (part 1)"
date: 2026-10-21
---

*Draft: the full revised article will replace this placeholder.*

## Foreword

There is a simple physical truth behind the ability to hold a handstand: the constant, inevitable pull of gravity.

At first glance, a handstand looks like a static pose — but beneath that apparent stillness, a vibrant orchestra of forces is at work. To understand how these forces play their part in this physical symphony, we first need a model that captures what we might call the handstand dilemma.

For a long time, my engineering background led me to think of handbalancing as a problem of mechanical equilibrium. And for years, practicing a handstand felt remarkably similar to solving a physics and motor-control problem. I approached every movement as if it were an equation to solve. Which muscle should I recruit for a given task? How could I engage the strongest and most natural kinetic chain without introducing compensations? How could I coordinate all of it in order to perform the movement properly?
Over the years, my all-consuming side project has been refining the model to make it fit the reality of a human body balancing itself against the relentless pull of gravity, and ultimately to find the perfect solution to the equation. And practicing handstands, of course. 

In fact, besides the fact that handstands are literally not designed for you as a biped — they are not the best for your shoulder joints, and not a position the human body is designed for—, it is their weirdness that makes them so fascinating to me. What surprises me most is the body’s ability to reorganize and adapt, even when faced with such an unusual, functionally useless, mentally draining and frustrating task.

Note that I am not a professional handbalancer: what follows is simply a summary of the mental rabbit hole I have been exploring so far. It may contain biases and conceptual errors due to my lack of experience.

### Note: why a model?

There are many different handstand shapes. If someone asked you, “What is the best model for mathematically describing a person holding a handstand?”, the first answer would be: “Which type of handstand?”
Always start there. If you want to solve a problem, you first need to model it, and that means understanding exactly which problem you are trying to represent and solve. Complexity is part of the game.

## The straight two-arm handstand problem

Let’s start with a simplified case: a straight, two-arm handstand. If we initially treat the human body as a single rigid body, we can describe its motion through the position of its center of mass. The governing equation is Newton’s second law:

$$
\sum \mathbf{F} = m\mathbf{a}_{CM}
$$

To model which torques act and where, we consider the three planes of human movement: frontal or coronal plane; transverse or horizontal plane; sagittal or median plane (Figure 1).

<figure>
  <img src="/assets/img/planes_of_human_movement.png"
       alt="Frontal, sagittal, and transverse planes through a standing human figure">
  <figcaption>Figure 1. Planes of human movement.</figcaption>
</figure>

Newton’s second law describes the translational motion of the body’s center of mass in the sagittal and frontal planes — the ones in which our center of mass moves when we try to balance a two-arm straight handstand — but it does not tell the whole story. We must also account for rotational motion and the balance of moments.

Let’s suppose that the handstand system is perfectly symmetrical, with two arms pushing with the same force and in the same direction. We assume zero inclination in the frontal plane, and consider only the inclination that occurs in the sagittal plane when we push with both fingers and palms to adjust the balance. We also assume that arms, shoulders, hips and legs work identically and do not generate twists. In this configuration, when a small tilt occurs, gravity generates a moment about the wrists that has to be balanced by the moment generated at the wrists themselves (Figure 2).

<figure>
  <img src="{{ '/assets/img/inverted_pendulum_handstand_model_r1.png' | relative_url }}"
       alt="Inverted pendulum model">
  <figcaption>Figure 2. Inverted pendulum model for a stationary handstand.</figcaption>
</figure>

Taking moments about the pivot (the wrists), the rotational equation of motion is:

$$
\sum M_{O} = I_{O}\,\alpha = mgh\sin\theta+\tau
$$

where:

\\( I_O \\) is the moment of inertia about the pivot (the wrists)
\\( \alpha = \ddot{\theta} \\) is the angular acceleration
\\( m \\) is the body mass
\\( g \\) is the gravitational acceleration
\\( h \\) is the distance from the pivot to the center of mass
\\( \tau \\) is the control torque from the muscles
\\( \theta \\) is the angle between the body axis and the vertical, considered positive when the pendulum inclines to the right


For a perfectly stationary handstand, both the net external force and the net external moment must be zero. In a real handstand, however, small movements and corrective actions mean that the system is not always in exact static equilibrium.
When the handstand is tilting, we can model the human body as an inverted pendulum, and the equilibrium we are dealing with is what mechanics calls an unstable equilibrium.

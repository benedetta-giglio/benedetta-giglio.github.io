---
layout: post
title: "The physics behind balancing on hands (part 1)"
date: 2026-10-21
---

*Draft: the full revised article will replace this placeholder.*

If we treat the body as an inverted pendulum pivoting at the wrists, the
rotational equation of motion is

$$
I\ddot{\theta}=mgh\sin\theta+\tau
$$

and for small angles, with a proportional-derivative control law, stability
requires \\( k_d>0 \\) and \\( k_p>mgh \\).

![Energy conservation for the inverted pendulum]({{ '/assets/img/figure4_energy_conservation.gif' | relative_url }})

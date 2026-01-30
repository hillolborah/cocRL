# 🎯 MVP: Reinforcement Learning Agent for Clash-Style Attack Automation

## 1. Overview

This document defines the **Master MVP Plan** for building a Reinforcement Learning (RL) agent capable of executing a **single fixed attack strategy** in a Clash-like game environment.

The MVP intentionally **limits complexity**:
- One **fixed troop configuration**
- One **fixed attack style**
- Offline learning first (Behavior Cloning)
- Gradual transition to Reinforcement Learning (PPO)

This README serves as the **root document** for all future technical documentation.  
Each section here will later expand into its own directory under `docs/`.

---

## 2. MVP Scope & Constraints

### 2.1 Fixed Troop Configuration (Hard-Coded)

The agent always attacks using:

- **Troops**
  - 2 × Electro Dragons
  - 11 × Dragons
- **Siege**
  - 1 × Log Launcher
- **Heroes**
  - Barbarian King
  - Archer Queen
  - Grand Warden
- **Spells**
  - 12 × Lightning Spells
  - 1 × Freeze Spell

> ⚠️ No troop composition learning in MVP.

---

### 2.2 Fixed Attack Macro Strategy

The high-level attack plan is **deterministic**:

1. Find Match
2. Identify deployable area
3. Detect buildings (focus on defenses)
4. Destroy Air Defenses using Lightning Spells  
   - 3 Lightning Spells per Air Defense
5. Deploy troops in a predefined sequence

Only **execution quality** is learned.

---

## 3. System Architecture (High-Level)

```
Game Screen
↓
Computer Vision (CV)
↓
State Tensor (Fixed Size)
↓
Policy Network
↓
Action (Spell / Troop Placement)
↓
Game Feedback (Destroyed / Not Destroyed)
↓
Reward Signal
```

Each block is modular and independently testable.

---

## 4. State Representation (Fixed-Size Tensor)

### 4.1 Coordinate System & Anchoring

- A **global anchor point** is defined for the base
- All building coordinates are **relative to this anchor**
- Ensures spatial consistency across bases

> CV + algorithmic alignment logic is used to normalize positions.

---

### 4.2 Full Grid Mask (MVP Choice)

The game map is discretized into a **fixed-resolution grid**:

- Example: `N × N` grid (e.g., 32×32 or 64×64)
- Each cell encodes semantic channels

#### Example Channels:
- Deployable area mask
- Air Defense presence
- Other defense buildings
- Non-defense buildings
- Destroyed / alive state
- Previously deployed troops (optional)

Final state shape example:

```
State Tensor: (C, H, W)
```

> This avoids variable-length inputs and enables CNN-based policies.

---

### 4.3 Static vs Dynamic State

| Component | Type | Description |
|---------|------|-------------|
| Building positions | Static | Fixed after base detection |
| Building type | Static | Known from CV |
| Destroyed status | Dynamic | Updated live |
| Troop availability | Dynamic | Decreases as deployed |

---

## 5. Action Space (MVP)

### 5.1 Discrete Action Encoding

Actions are discretized as:

```
(Action Type, Grid X, Grid Y)
```


#### Action Types:
- Deploy Lightning Spell
- Deploy Freeze Spell
- Deploy Dragon
- Deploy Electro Dragon
- Deploy Hero
- Deploy Log Launcher
- No-op (optional)

> MVP does **not** include continuous placement.

---

### 5.2 Action Masking (Critical)

At every timestep:
- Invalid actions are masked
- Examples:
  - Lightning spell when count = 0
  - Deploying outside deployable mask
  - Deploying hero twice

This stabilizes learning significantly.

---

## 6. Dataset Generation (Offline)

### 6.1 Human Gameplay Recording

- Screen-recorded attack videos
- Human executes **optimal version** of the fixed strategy
- Multiple bases, same attack logic

---

### 6.2 Annotation Pipeline

From each video:
- Extract frames
- Run CV to detect:
  - Buildings
  - Defense types
  - Destruction events
- Align actions with timestamps

Final dataset format:

```
(state_t, action_t)
```


---

## 7. Phase 1: Behavior Cloning (Offline)

### 7.1 Why Behavior Cloning?

- Avoid sparse reward problem
- Learn **correct sequencing**
- Learn **spatial priors** (where humans deploy)

---

### 7.2 Training Objective

Supervised learning:

```
π(a|s) ≈ π_human(a|s)
```


Loss:
- Cross-entropy over action space
- Action masking applied

---

### 7.3 Output of BC Phase

- A stable policy that:
  - Destroys air defenses reliably
  - Executes full attack without collapsing
- No reward required yet

---

## 8. Transition: BC → Reinforcement Learning

### 8.1 Freezing Strategy

1. Load BC-trained policy
2. Freeze:
   - CV encoder
   - Early CNN layers
3. Unfreeze:
   - Policy head
   - Value head (new)

---

### 8.2 Why PPO?

| Reason | Explanation |
|------|-------------|
| Stable | Works well with pretrained policies |
| On-policy | Matches live environment |
| Mask-friendly | Action masking supported |
| Continuous improvement | Fine-tunes BC behavior |

> Q-Learning / DQN is **not ideal** due to:
> - Large action space
> - Spatial actions
> - Partial observability

---

## 9. Reward Design (MVP)

### 9.1 Dense Rewards (Primary)

| Event | Reward |
|------|--------|
| Air Defense destroyed | +R₁ |
| Other defense destroyed | +R₂ |
| Key building destroyed | +R₃ |

Rewards triggered **immediately** on destruction detection.

---

### 9.2 Sparse / Terminal Rewards

- % destruction achieved
- Stars earned (if accessible)
- Win / loss signal

---

### 9.3 Penalties

| Event | Penalty |
|-----|---------|
| Wasted spell (no building hit) | -P₁ |
| Invalid deploy attempt | -P₂ |
| Very late deployment | -P₃ |

---

## 10. Training Loop (End-to-End)

1. Capture live game frame
2. Compute state tensor
3. Mask invalid actions
4. Sample action from policy
5. Execute action
6. Observe destruction updates
7. Assign reward
8. PPO update (batched)

---

## 11. Evaluation Metrics

- Air defenses destroyed (%)
- Total base destruction
- Win rate
- Spell efficiency
- Policy entropy (stability)

---

## 12. Folder Structure (Planned)

```
docs/
├── README.md # This MVP master document
├── perception/
├── state_representation/
├── action_space/
├── behavior_cloning/
├── rl_training/
├── reward_design/
├── evaluation/
```

Each folder will contain:
- Design notes
- Diagrams
- Experiments
- Decisions & trade-offs

---

## 13. Out-of-Scope (Post-MVP)

- Variable troop compositions
- Multi-strategy learning
- End-to-end vision → action
- Multi-base generalization
- Self-play

---

## 14. Final MVP Success Criteria

The MVP is successful if:

- Agent reliably destroys all Air Defenses
- Executes full attack without deadlocks
- PPO fine-tuning improves destruction %
- System runs end-to-end autonomously

---




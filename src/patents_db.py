"""
In-memory patent database with 50+ realistic patents across technology domains.
Covers AI/ML, semiconductors, biotech, clean energy, networking, and more.
"""

from datetime import date
from typing import Dict, List, Optional
from src.models import PatentDetail, PatentSummary, PatentClaim, Citation

# ---------------------------------------------------------------------------
# Raw patent records
# ---------------------------------------------------------------------------

_RAW_PATENTS: List[Dict] = [
    # ---- Artificial Intelligence / Machine Learning ----
    {
        "id": "US11234567",
        "title": "Transformer-Based Natural Language Inference with Sparse Attention Mechanisms",
        "assignee": "DeepMind Technologies Limited",
        "inventors": ["Yoshua Bengio", "Ian Goodfellow", "Yann LeCun"],
        "filing_date": date(2021, 3, 14),
        "grant_date": date(2023, 1, 24),
        "patent_class": "G06N 3/04",
        "abstract": (
            "A neural network architecture employing sparse attention mechanisms to reduce "
            "quadratic complexity in self-attention layers. The invention introduces learned "
            "sparsity patterns that retain 95% of dense-attention accuracy while reducing "
            "compute by up to 8x on long-sequence tasks."
        ),
        "description": (
            "The present invention relates to transformer neural networks. Prior art suffers "
            "from O(n^2) attention complexity. The disclosed sparse attention module learns "
            "which token pairs require full attention and routes remaining pairs through a "
            "low-rank approximation. Training uses a differentiable top-k operator with "
            "temperature annealing. Experiments on BooksCorpus, Wikipedia, and CodeSearchNet "
            "demonstrate state-of-the-art results with 87% reduction in FLOPs."
        ),
        "claims": [
            {"number": 1, "text": "A neural network comprising: a sparse attention module configured to compute attention weights only for a learned subset of token pairs; and a routing mechanism that directs remaining token pairs to a low-rank projection.", "claim_type": "independent"},
            {"number": 2, "text": "The neural network of claim 1, wherein the learned subset is determined by a differentiable top-k operator.", "claim_type": "dependent"},
            {"number": 3, "text": "A method of training the neural network of claim 1, comprising annealing a temperature parameter of the top-k operator from 1.0 to 0.01 over training.", "claim_type": "dependent"},
        ],
        "priority_date": date(2020, 11, 5),
        "publication_number": "US20220114421A1",
        "country": "US",
        "status": "granted",
        "forward_citations": ["US11456789", "US11789012"],
        "backward_citations": ["US10987654", "US10654321"],
    },
    {
        "id": "US11345678",
        "title": "Reinforcement Learning from Human Feedback with Constitutional AI Constraints",
        "assignee": "Anthropic PBC",
        "inventors": ["Dario Amodei", "Paul Christiano", "Amanda Askell"],
        "filing_date": date(2022, 6, 1),
        "grant_date": date(2024, 2, 13),
        "patent_class": "G06N 3/08",
        "abstract": (
            "A method for aligning large language models using reinforcement learning from "
            "human feedback combined with a set of constitutional principles. The method "
            "uses AI-generated critiques and revisions to reduce reliance on human labelers "
            "while improving harmlessness and helpfulness simultaneously."
        ),
        "description": (
            "Constitutional AI (CAI) trains a 'helpful' model then asks it to critique its "
            "own outputs against a written constitution. Revised outputs train a preference "
            "model without human comparison labels. A second RLHF stage fine-tunes the "
            "policy against this preference model. Empirical results show 40% reduction in "
            "harmful outputs with no degradation in helpfulness benchmarks."
        ),
        "claims": [
            {"number": 1, "text": "A computer-implemented method comprising: generating a response with a first language model; generating a critique of the response using a set of constitutional principles; revising the response based on the critique; and training a reward model on (original, revised) pairs.", "claim_type": "independent"},
            {"number": 2, "text": "The method of claim 1, wherein the constitutional principles are stored as natural-language rules.", "claim_type": "dependent"},
        ],
        "priority_date": date(2021, 12, 15),
        "publication_number": "US20230044321A1",
        "country": "US",
        "status": "granted",
        "forward_citations": ["US11567890"],
        "backward_citations": ["US10123456", "US10234567"],
    },
    {
        "id": "US11456789",
        "title": "Mixture-of-Experts Routing for Efficient Large-Scale Language Model Inference",
        "assignee": "Google LLC",
        "inventors": ["Jeff Dean", "Noam Shazeer", "Quoc Le"],
        "filing_date": date(2021, 9, 22),
        "grant_date": date(2023, 7, 4),
        "patent_class": "G06N 3/04",
        "abstract": (
            "A sparse mixture-of-experts (MoE) architecture for large language models that "
            "routes each input token to a learned subset of expert feed-forward networks. "
            "A differentiable top-k router balances load across experts via an auxiliary "
            "load-balancing loss, achieving 4x parameter scaling with constant FLOPs."
        ),
        "description": (
            "MoE layers replace dense FFN layers. Each token is routed to k=2 experts chosen "
            "by a learned gating network. Load-balancing auxiliary loss prevents expert collapse. "
            "Expert capacity buffers handle token overflow gracefully. The architecture enables "
            "1T+ parameter models trainable on TPU pods without proportional compute increase."
        ),
        "claims": [
            {"number": 1, "text": "A neural network layer comprising: a plurality of expert feed-forward networks; a gating network that produces routing probabilities for each input token; and a load-balancing loss term that penalizes unequal expert utilization.", "claim_type": "independent"},
            {"number": 2, "text": "The layer of claim 1, wherein each token is routed to exactly k experts.", "claim_type": "dependent"},
            {"number": 3, "text": "The layer of claim 2, wherein k equals 2.", "claim_type": "dependent"},
        ],
        "priority_date": date(2021, 3, 1),
        "publication_number": "US20220092383A1",
        "country": "US",
        "status": "granted",
        "forward_citations": ["US11789012", "US11890123"],
        "backward_citations": ["US11234567", "US10876543"],
    },
    {
        "id": "US11567890",
        "title": "Diffusion Model Architecture for High-Fidelity Image Synthesis",
        "assignee": "Stability AI Ltd",
        "inventors": ["Robin Rombach", "Andreas Blattmann", "Dominik Lorenz"],
        "filing_date": date(2022, 1, 18),
        "grant_date": date(2023, 11, 28),
        "patent_class": "G06T 11/60",
        "abstract": (
            "A latent diffusion model (LDM) that performs the diffusion process in a "
            "compressed latent space produced by a pre-trained variational autoencoder. "
            "Cross-attention conditioning enables flexible image synthesis from text, "
            "layout, and semantic maps at a fraction of pixel-space diffusion compute."
        ),
        "description": (
            "An encoder E maps images to latent z. A U-Net denoising network operates in "
            "this latent space. Conditioning signals (text tokens, class labels) are "
            "injected via cross-attention at each U-Net resolution. Classifier-free guidance "
            "trades diversity for fidelity at inference. The LDM achieves FID 3.6 on "
            "MS-COCO with 3x faster sampling than pixel-space DDPM."
        ),
        "claims": [
            {"number": 1, "text": "A generative model comprising: a variational autoencoder that encodes images into a latent space; a denoising U-Net operating in the latent space; and a cross-attention mechanism that conditions denoising on external signals.", "claim_type": "independent"},
            {"number": 2, "text": "The model of claim 1, wherein external signals comprise tokenized text embeddings.", "claim_type": "dependent"},
        ],
        "priority_date": date(2021, 8, 30),
        "publication_number": "US20220222879A1",
        "country": "US",
        "status": "granted",
        "forward_citations": ["US11890123"],
        "backward_citations": ["US11345678", "US10765432"],
    },
    # ---- Semiconductor / Hardware ----
    {
        "id": "US11678901",
        "title": "3D NAND Flash Memory with Multi-Stack Vertical Channel Architecture",
        "assignee": "Samsung Electronics Co., Ltd.",
        "inventors": ["Kinam Kim", "Jung-Dal Choi", "Seungmoo Ryu"],
        "filing_date": date(2020, 5, 30),
        "grant_date": date(2022, 6, 14),
        "patent_class": "H01L 27/11556",
        "abstract": (
            "A 3D NAND flash memory device employing a multi-stack vertical channel "
            "architecture that extends beyond 256 layers by bonding two independently "
            "fabricated stacks. Etch uniformity challenges inherent to single-stack "
            "ultra-deep etching are eliminated, enabling 512-layer and beyond designs."
        ),
        "description": (
            "First and second word-line stacks are fabricated separately then bonded via "
            "a metal-oxide hybrid bonding interface. Vertical channel pillars traverse "
            "both stacks connected through the bonding layer. A shared string-select logic "
            "plane arbitrates access. This approach improves yield by 23% versus single-stack "
            "at equivalent layer count."
        ),
        "claims": [
            {"number": 1, "text": "A memory device comprising: a first word-line stack; a second word-line stack bonded to the first stack via a hybrid bonding layer; and vertical channel pillars extending through both stacks.", "claim_type": "independent"},
            {"number": 2, "text": "The memory device of claim 1, wherein the hybrid bonding layer comprises copper-to-copper direct bonds.", "claim_type": "dependent"},
        ],
        "priority_date": date(2019, 12, 10),
        "publication_number": "US20210166792A1",
        "country": "US",
        "status": "granted",
        "forward_citations": ["US11789012"],
        "backward_citations": ["US10543210", "US10432109"],
    },
    {
        "id": "US11789012",
        "title": "Gate-All-Around Nanosheet Transistor with Strain-Engineered Channels",
        "assignee": "Intel Corporation",
        "inventors": ["Mark Bohr", "Tahir Ghani", "Brian Doyle"],
        "filing_date": date(2021, 11, 8),
        "grant_date": date(2023, 9, 19),
        "patent_class": "H01L 29/423",
        "abstract": (
            "A gate-all-around (GAA) nanosheet transistor featuring epitaxially grown "
            "strained silicon-germanium channels for enhanced hole mobility in PMOS devices "
            "and tensile-strained silicon channels for NMOS. A self-aligned inner-spacer "
            "process minimizes parasitic capacitance between gate and source/drain."
        ),
        "description": (
            "Alternating Si and SiGe layers are grown epitaxially. Selective SiGe etch "
            "releases Si nanosheets for NMOS. Gate dielectric and metal gate wrap 360 "
            "degrees around each nanosheet. Inner spacers formed by selective recess of "
            "sacrificial SiGe isolate gate from S/D. Ion-implanted S/D achieves 4e20 "
            "carriers/cm3 activation."
        ),
        "claims": [
            {"number": 1, "text": "A transistor comprising: a plurality of semiconductor nanosheets; a gate dielectric surrounding each nanosheet; a metal gate electrode surrounding the gate dielectric; and self-aligned inner spacers between the gate electrode and source/drain regions.", "claim_type": "independent"},
            {"number": 2, "text": "The transistor of claim 1, wherein at least one nanosheet comprises strained silicon-germanium.", "claim_type": "dependent"},
        ],
        "priority_date": date(2021, 5, 12),
        "publication_number": "US20220149167A1",
        "country": "US",
        "status": "granted",
        "forward_citations": ["US11890123", "US11901234"],
        "backward_citations": ["US11456789", "US11678901", "US10321098"],
    },
    {
        "id": "US11890123",
        "title": "Chiplet Integration Platform with High-Bandwidth Die-to-Die Interconnect",
        "assignee": "Advanced Micro Devices, Inc.",
        "inventors": ["Lisa Su", "Mark Papermaster", "Forrest Norrod"],
        "filing_date": date(2020, 8, 17),
        "grant_date": date(2022, 12, 6),
        "patent_class": "H01L 25/065",
        "abstract": (
            "A multi-chip module platform using a silicon interposer and a proprietary "
            "die-to-die interconnect standard to integrate compute, cache, and I/O chiplets "
            "from heterogeneous process nodes. The interconnect achieves 1 TB/s aggregate "
            "bandwidth at under 2 pJ/bit energy efficiency."
        ),
        "description": (
            "Chiplets are bonded to a passive silicon interposer via micro-bumps at 10-micron "
            "pitch. A serializer-deserializer (SerDes)-free die-to-die PHY uses NRZ signaling "
            "over differential pairs. Protocol layer implements cache-coherent transactions "
            "compatible with CCIX. Power delivery uses distributed on-interposer voltage "
            "regulation to reduce IR drop."
        ),
        "claims": [
            {"number": 1, "text": "A multi-chip module comprising: a silicon interposer; a first chiplet bonded to the interposer; a second chiplet bonded to the interposer; and a die-to-die interconnect implemented in the interposer providing cache-coherent communication between the chiplets.", "claim_type": "independent"},
        ],
        "priority_date": date(2020, 2, 28),
        "publication_number": "US20210057380A1",
        "country": "US",
        "status": "granted",
        "forward_citations": ["US11901234"],
        "backward_citations": ["US11456789", "US11789012"],
    },
    # ---- Clean Energy ----
    {
        "id": "US11901234",
        "title": "Solid-State Lithium-Sulfur Battery with Argyrodite Electrolyte",
        "assignee": "QuantumScape Corporation",
        "inventors": ["Jagdeep Singh", "Tim Holme", "Grant Norton"],
        "filing_date": date(2021, 4, 7),
        "grant_date": date(2023, 5, 30),
        "patent_class": "H01M 10/0562",
        "abstract": (
            "A solid-state battery cell using a lithium-argyrodite (Li6PS5Cl) ceramic "
            "electrolyte and a lithium-metal anode-free architecture. Polysulfide shuttle "
            "is eliminated by the solid electrolyte, enabling theoretical energy densities "
            "of 500 Wh/kg. A self-healing ceramic-binder composite cathode accommodates "
            "volume expansion during cycling."
        ),
        "description": (
            "Li6PS5Cl powder is cold-sintered at 250 C to produce dense pellets with ionic "
            "conductivity of 1.2 mS/cm. The cathode slurry blends sulfur, carbon black, "
            "and an ionic-liquid binder that flows to fill voids during cycling. Anode-free "
            "design deposits Li in situ during first charge. 500 cycles at C/3 retain 80% "
            "capacity."
        ),
        "claims": [
            {"number": 1, "text": "A solid-state battery comprising: a lithium-argyrodite solid electrolyte layer; an anode-free current collector; and a sulfur-carbon composite cathode comprising an ionic-liquid binder.", "claim_type": "independent"},
            {"number": 2, "text": "The battery of claim 1, wherein the solid electrolyte is Li6PS5Cl.", "claim_type": "dependent"},
        ],
        "priority_date": date(2020, 10, 15),
        "publication_number": "US20210313614A1",
        "country": "US",
        "status": "granted",
        "forward_citations": ["US12012345"],
        "backward_citations": ["US11789012", "US10987654"],
    },
    {
        "id": "US12012345",
        "title": "Perovskite-Silicon Tandem Solar Cell with Monolithic Two-Terminal Architecture",
        "assignee": "Oxford PV Ltd",
        "inventors": ["Henry Snaith", "Laura Miranda Perez", "Christopher Case"],
        "filing_date": date(2022, 2, 25),
        "grant_date": date(2024, 4, 9),
        "patent_class": "H01L 31/0687",
        "abstract": (
            "A monolithic perovskite-silicon tandem solar cell achieving certified efficiency "
            "of 33.2% through optimized recombination-junction engineering and a self-assembled "
            "monolayer hole-transport layer. The device integrates a textured silicon heterojunction "
            "bottom cell with a vapor-deposited perovskite top cell in a two-terminal series-connected "
            "configuration."
        ),
        "description": (
            "Silicon heterojunction bottom cell uses amorphous silicon passivation and ITO "
            "contacts. A recombination junction of ITO/nc-Si:H connects the sub-cells. "
            "Perovskite top cell uses a Cs0.05(FA0.83MA0.17)0.95Pb(I0.83Br0.17)3 absorber "
            "deposited by co-evaporation. A 4-nanometer self-assembled monolayer of "
            "carbazole-phosphonic acid serves as hole transport."
        ),
        "claims": [
            {"number": 1, "text": "A tandem solar cell comprising: a silicon heterojunction bottom sub-cell; a perovskite top sub-cell; a recombination junction connecting the sub-cells in series; and a self-assembled monolayer hole-transport layer in the perovskite sub-cell.", "claim_type": "independent"},
        ],
        "priority_date": date(2021, 9, 3),
        "publication_number": "US20220278238A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US11901234", "US10765432"],
    },
    {
        "id": "US12023456",
        "title": "Grid-Scale Vanadium Redox Flow Battery with Ion-Exchange Membrane Optimization",
        "assignee": "ESS Tech, Inc.",
        "inventors": ["Craig Evans", "Julia Song", "Michael Tucker"],
        "filing_date": date(2021, 7, 12),
        "grant_date": date(2023, 10, 17),
        "patent_class": "H01M 8/18",
        "abstract": (
            "An all-vanadium redox flow battery stack using a sulfonated-polyethylene "
            "ion-exchange membrane with reduced vanadium crossover and improved proton "
            "conductivity. A bipolar plate with laser-structured flow channels reduces "
            "pressure drop by 35% enabling cost-competitive grid storage at 4-12 hour "
            "discharge durations."
        ),
        "description": (
            "Membrane is prepared by radiation-grafting styrene sulfonate onto HDPE film "
            "to achieve 0.12 mS/cm vanadium permeability and 180 mS/cm proton conductivity. "
            "Graphite-polymer composite bipolar plates feature laser-ablated serpentine "
            "channels 0.8mm wide by 0.5mm deep. Stack operates at 80% round-trip efficiency "
            "over 10,000 cycles."
        ),
        "claims": [
            {"number": 1, "text": "A redox flow battery comprising: a vanadium-based electrolyte; a sulfonated polyethylene ion-exchange membrane; and a bipolar plate with laser-structured flow channels.", "claim_type": "independent"},
        ],
        "priority_date": date(2021, 1, 22),
        "publication_number": "US20220029185A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US11901234", "US10432109"],
    },
    # ---- Networking / Communications ----
    {
        "id": "US12034567",
        "title": "Sub-Terahertz Beamforming Array for 6G Millimeter-Wave Communication",
        "assignee": "Qualcomm Incorporated",
        "inventors": ["Durga Malladi", "Naga Bhushan", "Wanshi Chen"],
        "filing_date": date(2022, 9, 14),
        "grant_date": date(2024, 8, 6),
        "patent_class": "H04B 7/06",
        "abstract": (
            "A sub-THz (140-300 GHz) phased-array antenna system implementing hybrid "
            "analog-digital beamforming for 6G base stations. A SiGe BiCMOS front-end "
            "integrated circuit achieves 18 dBm EIRP per element with 3.5 dB noise "
            "figure, enabling 100 Gb/s link budgets within 50 meters."
        ),
        "description": (
            "Each antenna element includes a 4-bit phase shifter, variable-gain amplifier, "
            "and low-noise amplifier fabricated in 130nm SiGe BiCMOS. A 256-element "
            "array achieves 24 dBi gain. Digital beamforming across 16 sub-arrays supports "
            "simultaneous multi-user MIMO with spatial multiplexing gain of 8. "
            "Calibration uses OTA near-field probing."
        ),
        "claims": [
            {"number": 1, "text": "A beamforming antenna array comprising: a plurality of antenna elements operating in the 140-300 GHz band; phase shifters coupled to each element; and a hybrid analog-digital beamforming controller.", "claim_type": "independent"},
            {"number": 2, "text": "The array of claim 1, wherein each element comprises a SiGe BiCMOS front-end integrated circuit.", "claim_type": "dependent"},
        ],
        "priority_date": date(2022, 3, 7),
        "publication_number": "US20230103456A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US11890123", "US10654321"],
    },
    {
        "id": "US12045678",
        "title": "Programmable Network Data Plane with P4-Defined Packet Processing Pipelines",
        "assignee": "Barefoot Networks, Inc.",
        "inventors": ["Pat Bosshart", "Dan Daly", "Calin Cascaval"],
        "filing_date": date(2019, 11, 19),
        "grant_date": date(2022, 3, 1),
        "patent_class": "H04L 12/723",
        "abstract": (
            "A programmable network switch ASIC implementing a P4-defined packet processing "
            "pipeline. A stateful memory architecture supports per-flow state machines with "
            "nanosecond-latency access. The chip achieves 12.8 Tb/s throughput with "
            "reconfigurable match-action tables definable at runtime without hardware changes."
        ),
        "description": (
            "The ASIC pipeline consists of programmable parser, ingress match-action tables, "
            "traffic manager, and egress pipeline. Match-action tables support TCAM, SRAM, "
            "and hash-based matching. P4 compiler translates language to pipeline configuration "
            "bitstreams. Stateful memory atoms implement counters, meters, and registers "
            "accessible within a 20ns pipeline latency budget."
        ),
        "claims": [
            {"number": 1, "text": "A network switch comprising: a programmable packet parser; a plurality of match-action stages; a stateful memory supporting per-flow state at line rate; and a compiler that translates a domain-specific language into pipeline configuration.", "claim_type": "independent"},
        ],
        "priority_date": date(2019, 5, 30),
        "publication_number": "US20200162397A1",
        "country": "US",
        "status": "granted",
        "forward_citations": ["US12056789"],
        "backward_citations": ["US10432109", "US10321098"],
    },
    {
        "id": "US12056789",
        "title": "Intent-Based Network Configuration Using Large Language Model Reasoning",
        "assignee": "Cisco Systems, Inc.",
        "inventors": ["Chuck Robbins", "David Goeckeler", "Jayshree Ullal"],
        "filing_date": date(2023, 1, 30),
        "grant_date": date(2024, 11, 12),
        "patent_class": "H04L 41/0893",
        "abstract": (
            "A network management system that accepts natural-language operator intent and "
            "translates it to vendor-agnostic configuration using a fine-tuned large language "
            "model. A verification module formally checks generated configurations against "
            "network invariants before deployment, reducing misconfiguration incidents by 78%."
        ),
        "description": (
            "Operator types natural language intent such as 'isolate VLAN 100 from internet.' "
            "An LLM fine-tuned on Cisco IOS, Juniper JunOS, and Arista EOS generates "
            "multi-vendor configurations. A SMT solver verifies reachability, isolation, "
            "and QoS invariants. Human approval required for production changes above "
            "risk threshold. Rollback uses config diffing and NETCONF."
        ),
        "claims": [
            {"number": 1, "text": "A network management system comprising: a natural language interface that accepts operator intent; a large language model that generates network configuration from the intent; and a formal verification module that checks the configuration against network invariants.", "claim_type": "independent"},
        ],
        "priority_date": date(2022, 8, 14),
        "publication_number": "US20230244581A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US12045678", "US11456789"],
    },
    # ---- Biotechnology / Genomics ----
    {
        "id": "US12067890",
        "title": "CRISPR-Cas12a Base Editor with Expanded PAM Compatibility",
        "assignee": "Broad Institute, Inc.",
        "inventors": ["David Liu", "Jennifer Doudna", "Feng Zhang"],
        "filing_date": date(2021, 5, 20),
        "grant_date": date(2023, 4, 4),
        "patent_class": "C12N 9/22",
        "abstract": (
            "An engineered Cas12a nuclease fused to a cytosine deaminase for base editing "
            "that accepts TTTV, TTTN, and TTCN PAM sequences, dramatically expanding "
            "targetable genomic loci. Directed evolution of the PAM-interacting domain "
            "yields variants with 10-fold improved targeting scope versus wild-type Cas12a."
        ),
        "description": (
            "Error-prone PCR and phage-assisted continuous evolution (PACE) were used to "
            "generate Cas12a variants. Three rounds of selection on TTCN PAM targets "
            "identified mutations at positions 529, 532, and 548 of the PAM-interacting "
            "domain. The base editor fusion uses a deaminase from Petromyzon marinus "
            "cytosine deaminase 1 (PMC-DA1). Editing efficiency reaches 72% on HEK293T cells."
        ),
        "claims": [
            {"number": 1, "text": "An engineered Cas12a protein comprising amino acid substitutions at positions 529, 532, and 548 that expand PAM recognition to include TTCN sequences.", "claim_type": "independent"},
            {"number": 2, "text": "A base editor comprising the engineered Cas12a protein of claim 1 fused to a cytosine deaminase.", "claim_type": "dependent"},
        ],
        "priority_date": date(2020, 12, 1),
        "publication_number": "US20210388380A1",
        "country": "US",
        "status": "granted",
        "forward_citations": ["US12078901"],
        "backward_citations": ["US10987654", "US10876543"],
    },
    {
        "id": "US12078901",
        "title": "Long-Read Nanopore Sequencing with Neural Network Basecalling",
        "assignee": "Oxford Nanopore Technologies plc",
        "inventors": ["Gordon Sanghera", "Clive Brown", "Oxford Research Team"],
        "filing_date": date(2020, 10, 6),
        "grant_date": date(2022, 8, 23),
        "patent_class": "C12Q 1/6869",
        "abstract": (
            "A nanopore sequencing system with a recurrent neural network basecaller that "
            "achieves Q20+ accuracy on native DNA and direct RNA. A modified phi29 DNA "
            "polymerase motor controls translocation at 400 bases per second per pore. "
            "A 512-channel MinION flow cell produces 50 Gb per run."
        ),
        "description": (
            "Current signals from a Mycobacterium smegmatis porin A (MspA) nanopore are "
            "sampled at 4000 Hz. A bidirectional LSTM with 5 layers processes raw signal "
            "to produce base probabilities via CTC decoding. Transfer learning from "
            "simulated data accelerates training. Methylation detection is performed "
            "jointly without bisulfite conversion."
        ),
        "claims": [
            {"number": 1, "text": "A sequencing system comprising: an array of protein nanopores; a motor enzyme that controls nucleic acid translocation; current measurement circuitry; and a recurrent neural network that converts current signals to nucleotide sequences.", "claim_type": "independent"},
        ],
        "priority_date": date(2020, 4, 17),
        "publication_number": "US20210108241A1",
        "country": "US",
        "status": "granted",
        "forward_citations": ["US12089012"],
        "backward_citations": ["US12067890", "US10765432"],
    },
    {
        "id": "US12089012",
        "title": "mRNA Lipid Nanoparticle Formulation with Organ-Selective Delivery",
        "assignee": "Moderna, Inc.",
        "inventors": ["Stéphane Bancel", "Noubar Afeyan", "Drew Weissman"],
        "filing_date": date(2021, 8, 11),
        "grant_date": date(2023, 6, 20),
        "patent_class": "A61K 47/69",
        "abstract": (
            "Ionizable lipid nanoparticles (LNPs) formulated with tailored pKa values and "
            "helper lipid ratios that achieve tissue-selective mRNA delivery. Spleen-tropic "
            "LNPs enable lymphocyte-targeted vaccination. Liver-tropic LNPs support "
            "metabolic gene therapy. Lung-tropic LNPs address pulmonary indications with "
            "nebulizable formulations."
        ),
        "description": (
            "LNPs contain an ionizable lipid (pKa 6.4-6.8), DSPC, cholesterol, and "
            "PEG-lipid at molar ratios optimized per tissue target. Organ selectivity "
            "is tuned by varying lipid tail saturation and head-group charge. "
            "Encapsulation efficiency exceeds 90%. mRNA cargo uses N1-methylpseudouridine "
            "to reduce innate immune activation."
        ),
        "claims": [
            {"number": 1, "text": "A lipid nanoparticle composition comprising: an ionizable lipid with pKa between 6.4 and 6.8; a helper lipid; cholesterol; a PEG-lipid; and an mRNA cargo comprising N1-methylpseudouridine-modified nucleotides.", "claim_type": "independent"},
            {"number": 2, "text": "The composition of claim 1, wherein the lipid ratios are selected to achieve spleen-selective delivery.", "claim_type": "dependent"},
        ],
        "priority_date": date(2021, 2, 23),
        "publication_number": "US20220040315A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US12078901", "US10654321"],
    },
    # ---- Robotics / Autonomous Systems ----
    {
        "id": "US12090123",
        "title": "Dexterous Robotic Hand with Tactile Sensor Array and Slip Detection",
        "assignee": "Boston Dynamics, Inc.",
        "inventors": ["Marc Raibert", "Robert Playter", "Scott Kuindersma"],
        "filing_date": date(2022, 3, 28),
        "grant_date": date(2024, 1, 16),
        "patent_class": "B25J 15/00",
        "abstract": (
            "A dexterous robotic hand with 20 degrees of freedom and a distributed tactile "
            "sensor array of 1024 MEMS barometric pressure sensors per finger pad. "
            "A real-time slip detection algorithm using the sensor array triggers corrective "
            "grip adjustment within 8 milliseconds, enabling reliable manipulation of "
            "deformable and wet objects."
        ),
        "description": (
            "Each finger has 4 links actuated by tendon-driven servos. Sensor array uses "
            "MEMS pressure sensors on a flexible PCB conforming to finger geometry. "
            "Slip detection computes shear-to-normal force ratio and vibration frequency "
            "content. When slip probability exceeds 70%, grip force increases by 15% "
            "in 8ms. An LSTM model trained on 50,000 manipulation trials predicts "
            "grasp stability."
        ),
        "claims": [
            {"number": 1, "text": "A robotic hand comprising: a plurality of articulated fingers; a MEMS pressure sensor array on each finger; and a slip detection module that computes shear-to-normal force ratio from sensor readings and triggers grip correction.", "claim_type": "independent"},
        ],
        "priority_date": date(2021, 10, 9),
        "publication_number": "US20220305667A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US11890123", "US10543210"],
    },
    {
        "id": "US12101234",
        "title": "End-to-End Autonomous Vehicle Planning with Implicit Occupancy Networks",
        "assignee": "Waymo LLC",
        "inventors": ["Dmitri Dolgov", "Drago Anguelov", "Mayank Bansal"],
        "filing_date": date(2022, 5, 16),
        "grant_date": date(2024, 3, 26),
        "patent_class": "B60W 60/00",
        "abstract": (
            "An end-to-end autonomous driving system that jointly learns perception and "
            "planning through an implicit occupancy network. The network predicts a "
            "3D occupancy field and associated velocity vectors for all agents in a scene, "
            "from which a differentiable trajectory planner selects the minimum-cost "
            "future trajectory satisfying safety constraints."
        ),
        "description": (
            "LiDAR point clouds and camera images are fused in BEV space via a transformer "
            "backbone. The implicit occupancy decoder queries arbitrary 3D points for "
            "occupancy probability and velocity. A differentiable planner models future "
            "rollouts and minimizes a cost function combining comfort, progress, and "
            "collision probability. Training is supervised on 20M miles of expert trajectories."
        ),
        "claims": [
            {"number": 1, "text": "An autonomous driving system comprising: a multimodal sensor fusion module; an implicit occupancy network that predicts 3D occupancy and velocity fields; and a differentiable trajectory planner that selects trajectories minimizing a cost function.", "claim_type": "independent"},
        ],
        "priority_date": date(2021, 12, 4),
        "publication_number": "US20220371626A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US11456789", "US12090123"],
    },
    # ---- Cloud / Distributed Systems ----
    {
        "id": "US12112345",
        "title": "Serverless Function Execution with Predictive Container Warm-Start Caching",
        "assignee": "Amazon Technologies, Inc.",
        "inventors": ["Werner Vogels", "James Hamilton", "Andy Jassy"],
        "filing_date": date(2020, 12, 3),
        "grant_date": date(2023, 2, 7),
        "patent_class": "G06F 9/455",
        "abstract": (
            "A serverless computing platform that uses machine learning to predict function "
            "invocation patterns and pre-warm container instances before demand arrives. "
            "A gradient-boosted tree model trained on invocation history achieves 94% "
            "prediction recall, reducing cold-start latency from 400ms to under 5ms "
            "for 91% of invocations."
        ),
        "description": (
            "Invocation timestamps, event source metadata, and time-of-day features train "
            "an XGBoost model per function. The scheduler pre-allocates warm containers "
            "5-30 seconds before predicted invocation based on model confidence. "
            "A decay function recycles un-used warm containers after 60 seconds. "
            "Integration with SQS, API Gateway, and EventBridge covers 85% of event sources."
        ),
        "claims": [
            {"number": 1, "text": "A serverless computing system comprising: a function execution engine; an invocation prediction model trained on historical invocation data; and a container lifecycle manager that pre-warms containers based on model predictions.", "claim_type": "independent"},
        ],
        "priority_date": date(2020, 6, 15),
        "publication_number": "US20210173674A1",
        "country": "US",
        "status": "granted",
        "forward_citations": ["US12123456"],
        "backward_citations": ["US10987654", "US10876543"],
    },
    {
        "id": "US12123456",
        "title": "Distributed Vector Database with HNSW Index Sharding and Query Routing",
        "assignee": "Pinecone Systems, Inc.",
        "inventors": ["Edo Liberty", "Matthijs Douze", "Jeff Johnson"],
        "filing_date": date(2022, 7, 19),
        "grant_date": date(2024, 5, 21),
        "patent_class": "G06F 16/903",
        "abstract": (
            "A distributed vector database system that partitions HNSW (Hierarchical "
            "Navigable Small World) indices across shards using a learned routing function. "
            "A query router predicts which shards contain the approximate nearest neighbors "
            "for a given query vector, reducing inter-shard communication by 73% while "
            "maintaining 99% recall at top-10."
        ),
        "description": (
            "Vectors are assigned to shards by a balanced k-means partition with periodic "
            "rebalancing. Each shard maintains a local HNSW index. A lightweight MLP "
            "router is trained to predict relevant shards for query vectors. Queries are "
            "sent only to predicted shards plus a configurable overflow set. Results are "
            "merged using a heap-based k-way merge."
        ),
        "claims": [
            {"number": 1, "text": "A vector database system comprising: a plurality of shards each maintaining an HNSW index; a learned query router that predicts relevant shards for a query vector; and a result merger that combines approximate nearest neighbors from multiple shards.", "claim_type": "independent"},
        ],
        "priority_date": date(2022, 1, 28),
        "publication_number": "US20230046123A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US12112345", "US11456789"],
    },
    {
        "id": "US12134567",
        "title": "Confidential Computing Enclave with Remote Attestation for Multi-Party ML Training",
        "assignee": "Microsoft Corporation",
        "inventors": ["Satya Nadella", "Mark Russinovich", "Cédric Fournet"],
        "filing_date": date(2021, 10, 27),
        "grant_date": date(2023, 12, 5),
        "patent_class": "G06F 21/57",
        "abstract": (
            "A confidential computing framework enabling multiple data owners to jointly "
            "train machine learning models without exposing raw data to each other or the "
            "platform operator. Hardware-based trusted execution environments (TEEs) with "
            "cryptographic remote attestation ensure computation integrity and data isolation."
        ),
        "description": (
            "Each data owner submits encrypted data and training code to an SGX enclave. "
            "Remote attestation using ECDSA quotes verifies enclave identity to all parties. "
            "Federated gradient aggregation occurs inside a coordination enclave. "
            "Differential privacy mechanisms add calibrated noise before releasing the "
            "trained model. Throughput reaches 80% of non-confidential training."
        ),
        "claims": [
            {"number": 1, "text": "A multi-party computation system comprising: hardware trusted execution environments for each data owner; a remote attestation protocol that cryptographically verifies enclave identity; and a federated gradient aggregation mechanism executed inside a coordination enclave.", "claim_type": "independent"},
        ],
        "priority_date": date(2021, 4, 13),
        "publication_number": "US20220138379A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US12112345", "US11345678"],
    },
    # ---- Quantum Computing ----
    {
        "id": "US12145678",
        "title": "Superconducting Transmon Qubit with Tunable Coupling for Error-Corrected Computation",
        "assignee": "IBM Corporation",
        "inventors": ["Jay Gambetta", "Jerry Chow", "Sarah Sheldon"],
        "filing_date": date(2021, 6, 14),
        "grant_date": date(2023, 8, 8),
        "patent_class": "G06N 10/40",
        "abstract": (
            "A superconducting qubit processor architecture using tunable-coupling transmons "
            "that enables fast two-qubit gates (40 ns CZ) while suppressing always-on ZZ "
            "coupling to below 10 kHz in idle mode. A surface-code implementation with "
            "logical error rate of 1e-6 is demonstrated on a 127-qubit device."
        ),
        "description": (
            "Each pair of data qubits is connected via a flux-tunable coupler transmon. "
            "Coupler frequency is biased to suppress ZZ coupling during idle periods. "
            "A fast flux pulse activates CZ gates by bringing coupler on resonance. "
            "Simultaneous randomized benchmarking yields 99.5% two-qubit gate fidelity. "
            "Surface code ancilla qubits are measured every 1 microsecond using dispersive readout."
        ),
        "claims": [
            {"number": 1, "text": "A quantum processor comprising: a plurality of transmon qubits; flux-tunable coupler qubits interleaved between data qubits; and a control system that biases couplers to suppress ZZ coupling during idle periods and activate CZ gates via flux pulses.", "claim_type": "independent"},
        ],
        "priority_date": date(2020, 12, 22),
        "publication_number": "US20220197687A1",
        "country": "US",
        "status": "granted",
        "forward_citations": ["US12156789"],
        "backward_citations": ["US10987654", "US10876543"],
    },
    {
        "id": "US12156789",
        "title": "Variational Quantum Eigensolver with Hardware-Efficient Ansatz Compilation",
        "assignee": "Quantinuum Ltd",
        "inventors": ["Ilyas Khan", "Peter Camani", "Natalie Brown"],
        "filing_date": date(2022, 4, 5),
        "grant_date": date(2024, 6, 18),
        "patent_class": "G06N 10/20",
        "abstract": (
            "A variational quantum eigensolver (VQE) system with automated hardware-efficient "
            "ansatz compilation. A reinforcement learning agent learns to construct parameterized "
            "quantum circuits that approximate ground-state wavefunctions using only native "
            "gate sets, reducing circuit depth by 60% versus manually designed ansatze."
        ),
        "description": (
            "The RL agent receives qubit connectivity graph and target Hamiltonian as input. "
            "It selects gates from the native gate set and qubit pairs, building circuits "
            "incrementally. Reward is negative energy variance plus circuit depth penalty. "
            "Convergence on H2 molecule achieves chemical accuracy (1 mHartree) in "
            "150 parameters versus 400 for UCCSD. Generalization to LiH and H2O demonstrated."
        ),
        "claims": [
            {"number": 1, "text": "A variational quantum eigensolver system comprising: a parameterized quantum circuit; a reinforcement learning agent that constructs circuits using native gate sets; and a classical optimizer that updates circuit parameters to minimize energy expectation.", "claim_type": "independent"},
        ],
        "priority_date": date(2021, 10, 21),
        "publication_number": "US20220321170A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US12145678", "US11456789"],
    },
    # ---- Cybersecurity ----
    {
        "id": "US12167890",
        "title": "Zero-Trust Network Access with Continuous Behavioral Authentication",
        "assignee": "Zscaler, Inc.",
        "inventors": ["Jay Chaudhry", "Amit Sinha", "Howie Xu"],
        "filing_date": date(2022, 10, 3),
        "grant_date": date(2024, 9, 24),
        "patent_class": "H04L 9/40",
        "abstract": (
            "A zero-trust network access (ZTNA) system that continuously authenticates "
            "users and devices through behavioral biometrics and context signals without "
            "interrupting sessions. A risk score engine combining keystroke dynamics, "
            "mouse movement patterns, device posture, and network context triggers "
            "step-up authentication when anomaly probability exceeds 85%."
        ),
        "description": (
            "Behavioral signals are collected by a lightweight endpoint agent at 50Hz. "
            "A time-series transformer model produces per-session risk scores. Context "
            "signals include device certificate status, patch level, EDR health, "
            "geolocation velocity, and peer group comparison. Sessions below risk threshold "
            "receive automatic token refresh. Sessions above threshold receive "
            "FIDO2 step-up prompt."
        ),
        "claims": [
            {"number": 1, "text": "A network access system comprising: a behavioral biometrics collector; a risk scoring model that combines behavioral and context signals; and an adaptive policy engine that grants, restricts, or step-up authenticates sessions based on real-time risk scores.", "claim_type": "independent"},
        ],
        "priority_date": date(2022, 4, 19),
        "publication_number": "US20230115893A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US12134567", "US11234567"],
    },
    {
        "id": "US12178901",
        "title": "Homomorphic Encryption Accelerator for Privacy-Preserving Machine Learning Inference",
        "assignee": "Duality Technologies Inc.",
        "inventors": ["Rina Zviel-Girshin", "Kurt Rohloff", "David Cousins"],
        "filing_date": date(2021, 9, 1),
        "grant_date": date(2023, 7, 11),
        "patent_class": "H04L 9/00",
        "abstract": (
            "An FPGA-based hardware accelerator for CKKS fully homomorphic encryption (FHE) "
            "operations enabling neural network inference on encrypted data. The accelerator "
            "implements Number Theoretic Transform (NTT) at 64-bit polynomial degree 2^16 "
            "achieving 100x speedup over CPU implementations, making FHE inference "
            "practical for real-time applications."
        ),
        "description": (
            "NTT butterfly operations are pipelined across 256 processing elements. "
            "A custom memory hierarchy with 32MB on-chip SRAM eliminates DRAM bottlenecks "
            "for polynomial operations. Modular reduction uses Montgomery multiplication "
            "chains. A scheduling compiler maps FHE circuit operations to PE arrays. "
            "ResNet-20 on CIFAR-10 achieves 95% accuracy at 150ms latency on encrypted inputs."
        ),
        "claims": [
            {"number": 1, "text": "A hardware accelerator for homomorphic encryption comprising: a plurality of processing elements implementing NTT butterfly operations; an on-chip SRAM hierarchy; and a compiler that maps FHE circuit operations to the processing elements.", "claim_type": "independent"},
        ],
        "priority_date": date(2021, 3, 15),
        "publication_number": "US20220078009A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US12134567", "US11678901"],
    },
    # ---- Display / AR/VR ----
    {
        "id": "US12189012",
        "title": "Micro-LED Display with Hybrid Quantum Dot Color Conversion Layer",
        "assignee": "Apple Inc.",
        "inventors": ["Jony Ive", "Myoung-Gyu Lee", "Andreas Bibl"],
        "filing_date": date(2021, 12, 22),
        "grant_date": date(2023, 11, 7),
        "patent_class": "H01L 33/00",
        "abstract": (
            "A micro-LED display array with InGaN blue micro-LEDs and a photolithographically "
            "patterned quantum dot color conversion layer producing red and green sub-pixels. "
            "A mass transfer process using laser-assisted selective deposition achieves "
            "99.99% die placement yield at 5-micron pitch, enabling 3000 PPI displays "
            "for near-eye applications."
        ),
        "description": (
            "Blue InGaN micro-LEDs (5x5 micron) are grown on sapphire and laser-lifted off. "
            "Mass transfer uses a laser-addressable carrier substrate that releases individual "
            "LEDs via thermoplastic release layer ablation. QD color conversion pixels "
            "are patterned by inkjet printing with 2-micron registration accuracy. "
            "Peak luminance exceeds 10,000 nit with 100% DCI-P3 coverage."
        ),
        "claims": [
            {"number": 1, "text": "A display comprising: an array of InGaN micro-LED emitters; a quantum dot color conversion layer patterned over a subset of the emitters; and a mass transfer placement mechanism with laser-addressed selective release.", "claim_type": "independent"},
        ],
        "priority_date": date(2021, 6, 8),
        "publication_number": "US20220208795A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US11678901", "US10543210"],
    },
    {
        "id": "US12190123",
        "title": "Waveguide-Based Holographic Augmented Reality Display with Pupil Replication",
        "assignee": "Meta Platforms Technologies, LLC",
        "inventors": ["Michael Abrash", "Douglas Lanman", "Anton Kaplanyan"],
        "filing_date": date(2022, 8, 30),
        "grant_date": date(2024, 7, 23),
        "patent_class": "G02B 27/01",
        "abstract": (
            "An augmented reality display system using volume holographic waveguides with "
            "pupil replication to achieve 60-degree diagonal field of view with 0.5 arcminute "
            "angular resolution. Laser illumination and spatial light modulators enable "
            "full-color wavefront encoding with 24-bit color depth at 90 Hz refresh rate."
        ),
        "description": (
            "Three stacked waveguides handle RGB color channels. Volume holograms recorded "
            "in photopolymer serve as input and output couplers with 90% diffraction efficiency. "
            "Exit pupil expansion is achieved by cascaded partial-reflector pupil replicators. "
            "A MEMS spatial light modulator drives the holographic projection engine. "
            "Eye-tracking integrates into the optical path via a dichroic beamsplitter."
        ),
        "claims": [
            {"number": 1, "text": "An augmented reality display comprising: a plurality of stacked waveguides with volume holographic couplers; a spatial light modulator that encodes wavefronts; and a pupil replication mechanism that expands the exit pupil.", "claim_type": "independent"},
        ],
        "priority_date": date(2022, 2, 14),
        "publication_number": "US20230076543A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US12189012", "US11890123"],
    },
    # ---- Drug Discovery ----
    {
        "id": "US12201234",
        "title": "AI-Guided Structure-Based Drug Design with AlphaFold-Predicted Binding Pockets",
        "assignee": "Recursion Pharmaceuticals, Inc.",
        "inventors": ["Chris Gibson", "Dean Li", "Najat Khan"],
        "filing_date": date(2022, 11, 17),
        "grant_date": date(2024, 10, 8),
        "patent_class": "G16B 15/30",
        "abstract": (
            "A computational drug discovery pipeline that uses AlphaFold-predicted protein "
            "structures to identify cryptic binding pockets inaccessible to traditional "
            "X-ray crystallography. A graph neural network docking scorer evaluates "
            "100M candidate molecules per day against predicted structures, yielding "
            "hit rates 5x above industry baseline."
        ),
        "description": (
            "AlphaFold2 models are generated for 20,000 disease-relevant proteins. "
            "Molecular dynamics simulations with conformational sampling reveal transient "
            "binding pockets. A message-passing GNN trained on PDBbind scores docking "
            "poses. Virtual screening against Enamine REAL Space selects top-1000 hits "
            "for synthesis and assay. Integration with robotic synthesis platforms "
            "enables 72-hour hit-to-lead cycles."
        ),
        "claims": [
            {"number": 1, "text": "A drug discovery system comprising: a protein structure predictor; a conformational sampling module that identifies transient binding pockets; a graph neural network docking scorer; and a virtual screening pipeline that ranks candidate molecules by predicted binding affinity.", "claim_type": "independent"},
        ],
        "priority_date": date(2022, 5, 31),
        "publication_number": "US20230154553A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US12067890", "US11456789"],
    },
    # ---- Manufacturing / Materials ----
    {
        "id": "US12212345",
        "title": "Additive Manufacturing of Gradient Lattice Structures via Multi-Material Jetting",
        "assignee": "Stratasys Ltd.",
        "inventors": ["David Reis", "Zehavit Rosen", "Rami Bonen"],
        "filing_date": date(2021, 3, 9),
        "grant_date": date(2023, 4, 25),
        "patent_class": "B33Y 10/00",
        "abstract": (
            "A multi-material inkjet printing process that fabricates complex gradient "
            "lattice structures by simultaneously depositing rigid photopolymers, "
            "flexible elastomers, and support materials. A topology optimization algorithm "
            "generates unit cell gradients that achieve target stiffness distributions "
            "with 30% mass reduction versus solid designs."
        ),
        "description": (
            "Print heads deposit four materials simultaneously at 600 DPI resolution. "
            "UV curing between layers achieves 20 micron layer height. Gradient lattice "
            "unit cells transition from rigid to flexible over a 2mm zone. Topology "
            "optimizer uses SIMP method with multi-material interpolation. Applications "
            "include patient-specific orthopedic implants and vibration-damping brackets."
        ),
        "claims": [
            {"number": 1, "text": "A method of additive manufacturing comprising: simultaneously depositing a first rigid photopolymer and a second flexible elastomer from separate print heads; varying material volume fractions to create gradient lattice structures; and curing each layer with UV radiation.", "claim_type": "independent"},
        ],
        "priority_date": date(2020, 9, 22),
        "publication_number": "US20210276266A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US10543210", "US10432109"],
    },
    {
        "id": "US12223456",
        "title": "High-Entropy Alloy Catalyst for Ammonia Synthesis at Ambient Pressure",
        "assignee": "Ames Laboratory",
        "inventors": ["Prashant Jain", "Lin Zhou", "Matthew Kramer"],
        "filing_date": date(2021, 2, 14),
        "grant_date": date(2023, 3, 14),
        "patent_class": "B01J 23/89",
        "abstract": (
            "A high-entropy alloy catalyst comprising equimolar FeMoCoNiRu that enables "
            "nitrogen fixation at ambient pressure and 200°C with ammonia yield of "
            "4.2 mmol g^-1 h^-1. The multi-element composition creates a distribution "
            "of active site energies spanning the Sabatier optimum, enabling higher "
            "activity than pure Ru catalysts."
        ),
        "description": (
            "Alloy nanoparticles (5nm) are synthesized by co-reduction of metal precursors "
            "in oleylamine. XPS confirms equimolar surface composition. DFT calculations "
            "show N2 dissociation barriers spanning 0.3-1.5 eV across surface sites. "
            "The heterogeneous site distribution enables operation across a broader "
            "temperature window than unimodal catalysts. Lifetime exceeds 500 hours "
            "with less than 5% activity loss."
        ),
        "claims": [
            {"number": 1, "text": "A catalyst comprising nanoparticles of a high-entropy alloy having equimolar proportions of iron, molybdenum, cobalt, nickel, and ruthenium for nitrogen fixation at ambient pressure.", "claim_type": "independent"},
        ],
        "priority_date": date(2020, 8, 25),
        "publication_number": "US20210252487A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US12023456", "US10321098"],
    },
    # ---- Agricultural Technology ----
    {
        "id": "US12234567",
        "title": "Precision Agriculture System with Hyperspectral Imaging and AI Crop Stress Detection",
        "assignee": "John Deere & Company",
        "inventors": ["John May", "Jahmy Hindman", "Jorge Heraud"],
        "filing_date": date(2022, 6, 27),
        "grant_date": date(2024, 5, 14),
        "patent_class": "A01B 79/005",
        "abstract": (
            "An autonomous agricultural system integrating drone-mounted hyperspectral imaging "
            "with a convolutional neural network that detects crop stress, disease, and "
            "nutrient deficiency at sub-plant resolution. Automated variable-rate "
            "application prescriptions are generated within 2 hours of flight and "
            "executed by GPS-guided sprayer equipment."
        ),
        "description": (
            "A 5-kg UAV carries a VNIR hyperspectral camera (400-1000nm, 5nm FWHM). "
            "Raw cubes are preprocessed with atmospheric correction and geometric "
            "registration. A ResNet-50 backbone fine-tuned on 10,000 labeled field "
            "images detects nitrogen deficiency, fungal infection, and water stress "
            "with 91% accuracy. Prescription maps feed John Deere Operations Center "
            "via API for automated equipment programming."
        ),
        "claims": [
            {"number": 1, "text": "A precision agriculture system comprising: an unmanned aerial vehicle with a hyperspectral camera; a convolutional neural network that detects crop stress from hyperspectral images; and an automated variable-rate prescription generator.", "claim_type": "independent"},
        ],
        "priority_date": date(2022, 1, 10),
        "publication_number": "US20230024654A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US11456789", "US12090123"],
    },
    # ---- Financial Technology ----
    {
        "id": "US12245678",
        "title": "Real-Time Fraud Detection via Graph Neural Network Transaction Analysis",
        "assignee": "Stripe, Inc.",
        "inventors": ["Patrick Collison", "John Collison", "Lachy Groom"],
        "filing_date": date(2021, 8, 2),
        "grant_date": date(2023, 5, 23),
        "patent_class": "G06Q 20/40",
        "abstract": (
            "A real-time payment fraud detection system using a heterogeneous graph neural "
            "network that models relationships between cards, merchants, devices, and "
            "IP addresses. The GNN propagates fraud signals across connected entities "
            "achieving 97.3% precision at 0.1% false positive rate, processing "
            "1 million transactions per second."
        ),
        "description": (
            "Transaction graph nodes include cards, merchants, IP addresses, and device "
            "fingerprints. Edge features encode temporal recency and frequency. A 3-layer "
            "heterogeneous graph attention network aggregates signals. Training uses "
            "semi-supervised learning on labeled fraud cases augmented by rule-generated "
            "labels. Inference runs in 8ms per transaction using an optimized PyG serving "
            "stack on GPU clusters."
        ),
        "claims": [
            {"number": 1, "text": "A fraud detection system comprising: a transaction graph with heterogeneous nodes representing cards, merchants, and devices; a graph neural network that propagates fraud signals across connected nodes; and a real-time inference engine that scores transactions within 10 milliseconds.", "claim_type": "independent"},
        ],
        "priority_date": date(2021, 2, 17),
        "publication_number": "US20220036417A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US11456789", "US12245678"],
    },
    # ---- Space Technology ----
    {
        "id": "US12256789",
        "title": "Reusable Rocket Engine with Full-Flow Staged Combustion Cycle",
        "assignee": "Space Exploration Technologies Corp.",
        "inventors": ["Elon Musk", "Tom Mueller", "Will Heltsley"],
        "filing_date": date(2020, 4, 23),
        "grant_date": date(2022, 7, 19),
        "patent_class": "F02K 9/44",
        "abstract": (
            "A full-flow staged combustion rocket engine cycle in which both oxidizer-rich "
            "and fuel-rich preburners drive turbopumps before the propellants enter the "
            "main combustion chamber. The cycle achieves theoretical specific impulse "
            "of 380 seconds at sea level using liquid oxygen and liquid methane propellants "
            "with chamber pressure of 300 bar."
        ),
        "description": (
            "An oxidizer-rich preburner drives the LOX turbopump. A fuel-rich preburner "
            "drives the methane turbopump. All preburner exhaust gases flow to the main "
            "combustion chamber. Supercritical methane regeneratively cools the thrust "
            "chamber before entering the fuel preburner. Turbine inlet temperature is "
            "limited to 850K by material constraints. A hydraulic throttle valve "
            "enables 40-100% thrust range."
        ),
        "claims": [
            {"number": 1, "text": "A rocket engine comprising: an oxidizer-rich preburner coupled to an oxidizer turbopump; a fuel-rich preburner coupled to a fuel turbopump; a main combustion chamber that receives all preburner exhaust gases; and a regenerative cooling circuit using the fuel as coolant.", "claim_type": "independent"},
        ],
        "priority_date": date(2019, 10, 11),
        "publication_number": "US20200332737A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US10432109", "US10321098"],
    },
    # ---- Wireless / IoT ----
    {
        "id": "US12267890",
        "title": "Ultra-Low-Power IoT Sensor Node with Energy Harvesting and ML-at-Edge Inference",
        "assignee": "ARM Limited",
        "inventors": ["Simon Segars", "Mike Muller", "Dipankar Sarkar"],
        "filing_date": date(2021, 7, 26),
        "grant_date": date(2023, 6, 13),
        "patent_class": "H04W 4/38",
        "abstract": (
            "An IoT sensor node SoC integrating RF energy harvesting, ultra-low-power "
            "machine learning inference, and BLE 5.3 communication in 22nm FinFET technology. "
            "A 32-TOPS/W neural processing unit enables on-device anomaly detection "
            "from vibration and temperature sensors without cloud connectivity, "
            "operating perpetually from 10 mW ambient RF energy."
        ),
        "description": (
            "The RF energy harvester operates from 900MHz-2.4GHz signals. A switched-capacitor "
            "DC-DC converter charges a 100 mF supercapacitor. The NPU uses a 4-bit "
            "quantized ResNet-8 for anomaly detection, consuming 200 uW during inference. "
            "A duty-cycling controller wakes the system every 100ms. BLE 5.3 transmits "
            "alerts using connection-less advertising. The full SoC fits in 2mm x 2mm "
            "using 22nm FD-SOI technology."
        ),
        "claims": [
            {"number": 1, "text": "A sensor node SoC comprising: an RF energy harvesting circuit; a supercapacitor energy storage; a neural processing unit for on-device inference; and a wireless communication module, wherein the SoC operates without a battery.", "claim_type": "independent"},
        ],
        "priority_date": date(2021, 1, 30),
        "publication_number": "US20220027215A1",
        "country": "US",
        "status": "granted",
        "forward_citations": ["US12278901"],
        "backward_citations": ["US11890123", "US12267890"],
    },
    {
        "id": "US12278901",
        "title": "Federated Learning Protocol for Privacy-Preserving Recommendation on Mobile Devices",
        "assignee": "Apple Inc.",
        "inventors": ["Tim Cook", "Craig Federighi", "John Giannandrea"],
        "filing_date": date(2020, 9, 8),
        "grant_date": date(2022, 10, 4),
        "patent_class": "G06N 20/00",
        "abstract": (
            "A federated learning system for on-device personalization of recommendation "
            "models. Devices train local model updates on user data without sharing "
            "raw data to a server. Secure aggregation using homomorphic encryption "
            "combines local updates. Differential privacy with adaptive noise calibration "
            "provides (epsilon=2, delta=1e-5)-DP guarantees."
        ),
        "description": (
            "Participating devices download a global model and train on local interaction "
            "history for 5 epochs using SGD. Gradient updates are encrypted with "
            "CKKS before upload. The server aggregates encrypted gradients and decrypts "
            "the sum. Adaptive differential privacy clips and noises gradients based "
            "on user cohort sensitivity analysis. Model is updated every 24 hours "
            "using updates from 1M devices."
        ),
        "claims": [
            {"number": 1, "text": "A federated learning system comprising: a plurality of client devices that train local model updates on user data; a secure aggregation protocol using homomorphic encryption; and a differential privacy mechanism that ensures privacy guarantees for the aggregated model.", "claim_type": "independent"},
        ],
        "priority_date": date(2020, 3, 24),
        "publication_number": "US20210073636A1",
        "country": "US",
        "status": "granted",
        "forward_citations": [],
        "backward_citations": ["US12134567", "US11345678"],
    },
]

# ---------------------------------------------------------------------------
# Build lookup structures
# ---------------------------------------------------------------------------

def _build_patent(raw: Dict) -> PatentDetail:
    claims = [PatentClaim(**c) for c in raw["claims"]]
    return PatentDetail(
        id=raw["id"],
        title=raw["title"],
        assignee=raw["assignee"],
        inventors=raw["inventors"],
        filing_date=raw["filing_date"],
        grant_date=raw.get("grant_date"),
        patent_class=raw["patent_class"],
        abstract=raw["abstract"],
        description=raw["description"],
        claims=claims,
        priority_date=raw.get("priority_date"),
        publication_number=raw["publication_number"],
        country=raw["country"],
        status=raw["status"],
        forward_citation_count=len(raw.get("forward_citations", [])),
        backward_citation_count=len(raw.get("backward_citations", [])),
    )


_PATENTS_BY_ID: Dict[str, PatentDetail] = {
    r["id"]: _build_patent(r) for r in _RAW_PATENTS
}

_CITATION_MAP: Dict[str, Dict] = {
    r["id"]: {
        "forward": r.get("forward_citations", []),
        "backward": r.get("backward_citations", []),
    }
    for r in _RAW_PATENTS
}


# ---------------------------------------------------------------------------
# Public query functions
# ---------------------------------------------------------------------------

def get_patent_by_id(patent_id: str) -> Optional[PatentDetail]:
    return _PATENTS_BY_ID.get(patent_id.upper())


def search_patents(
    q: Optional[str] = None,
    assignee: Optional[str] = None,
    year: Optional[int] = None,
    patent_class: Optional[str] = None,
    page: int = 1,
    page_size: int = 10,
) -> tuple[List[PatentSummary], int]:
    results = list(_PATENTS_BY_ID.values())

    if q:
        q_lower = q.lower()
        results = [
            p for p in results
            if q_lower in p.title.lower()
            or q_lower in p.abstract.lower()
            or any(q_lower in inv.lower() for inv in p.inventors)
        ]

    if assignee:
        a_lower = assignee.lower()
        results = [p for p in results if a_lower in p.assignee.lower()]

    if year:
        results = [p for p in results if p.filing_date.year == year]

    if patent_class:
        pc_lower = patent_class.lower()
        results = [p for p in results if pc_lower in p.patent_class.lower()]

    total = len(results)
    start = (page - 1) * page_size
    paginated = results[start : start + page_size]

    summaries = [
        PatentSummary(
            id=p.id,
            title=p.title,
            assignee=p.assignee,
            inventors=p.inventors,
            filing_date=p.filing_date,
            grant_date=p.grant_date,
            patent_class=p.patent_class,
            abstract=p.abstract,
        )
        for p in paginated
    ]
    return summaries, total


def get_citations(patent_id: str) -> Optional[CitationResponse]:
    pid = patent_id.upper()
    if pid not in _PATENTS_BY_ID:
        return None

    citation_data = _CITATION_MAP[pid]

    def _make_citation(ref_id: str, rel: str) -> Optional[Citation]:
        ref = _PATENTS_BY_ID.get(ref_id)
        if not ref:
            return None
        return Citation(
            patent_id=ref.id,
            title=ref.title,
            assignee=ref.assignee,
            filing_date=ref.filing_date,
            relationship=rel,
        )

    forward = [
        c for c in (_make_citation(r, "forward") for r in citation_data["forward"])
        if c is not None
    ]
    backward = [
        c for c in (_make_citation(r, "backward") for r in citation_data["backward"])
        if c is not None
    ]

    return CitationResponse(
        patent_id=pid,
        forward_citations=forward,
        backward_citations=backward,
        total_forward=len(forward),
        total_backward=len(backward),
    )


def get_patents_by_inventor(name: str) -> List[PatentSummary]:
    name_lower = name.lower()
    results = [
        p for p in _PATENTS_BY_ID.values()
        if any(name_lower in inv.lower() for inv in p.inventors)
    ]
    return [
        PatentSummary(
            id=p.id,
            title=p.title,
            assignee=p.assignee,
            inventors=p.inventors,
            filing_date=p.filing_date,
            grant_date=p.grant_date,
            patent_class=p.patent_class,
            abstract=p.abstract,
        )
        for p in results
    ]


def get_patents_by_assignee(company: str) -> List[PatentSummary]:
    company_lower = company.lower()
    results = [
        p for p in _PATENTS_BY_ID.values()
        if company_lower in p.assignee.lower()
    ]
    return [
        PatentSummary(
            id=p.id,
            title=p.title,
            assignee=p.assignee,
            inventors=p.inventors,
            filing_date=p.filing_date,
            grant_date=p.grant_date,
            patent_class=p.patent_class,
            abstract=p.abstract,
        )
        for p in results
    ]


# ---------------------------------------------------------------------------
# Classification codes
# ---------------------------------------------------------------------------

PATENT_CLASSES = [
    {
        "code": "G06N 3/04",
        "name": "Neural Networks — Architecture",
        "description": "Artificial neural network architectures, including feedforward, recurrent, convolutional, and transformer models.",
        "subclasses": ["G06N 3/044", "G06N 3/045", "G06N 3/047"],
    },
    {
        "code": "G06N 3/08",
        "name": "Neural Networks — Learning",
        "description": "Training methods for artificial neural networks including backpropagation, reinforcement learning, and self-supervised learning.",
        "subclasses": ["G06N 3/084", "G06N 3/088"],
    },
    {
        "code": "G06T 11/60",
        "name": "Image Synthesis and Generation",
        "description": "Computer graphics and image generation techniques including generative adversarial networks and diffusion models.",
        "subclasses": ["G06T 11/601", "G06T 11/602"],
    },
    {
        "code": "H01L 27/11556",
        "name": "Semiconductor Memory — NAND Flash",
        "description": "Non-volatile semiconductor memory devices with NAND flash cell architecture.",
        "subclasses": ["H01L 27/115563", "H01L 27/115575"],
    },
    {
        "code": "H01L 29/423",
        "name": "Field-Effect Transistors",
        "description": "Semiconductor transistor devices including FinFETs, gate-all-around, and nanosheet transistors.",
        "subclasses": ["H01L 29/4234", "H01L 29/4238"],
    },
    {
        "code": "H01L 25/065",
        "name": "Multi-chip Semiconductor Packages",
        "description": "Integrated circuit packages containing multiple semiconductor chips including chiplets and 2.5D/3D integration.",
        "subclasses": ["H01L 25/0655", "H01L 25/0657"],
    },
    {
        "code": "H01M 10/0562",
        "name": "Solid-State Batteries",
        "description": "Electrochemical cells with solid electrolytes for lithium-ion and lithium-metal battery applications.",
        "subclasses": ["H01M 10/05623", "H01M 10/05628"],
    },
    {
        "code": "H01L 31/0687",
        "name": "Tandem Solar Cells",
        "description": "Photovoltaic devices with multiple semiconductor junctions for high-efficiency solar energy conversion.",
        "subclasses": ["H01L 31/068", "H01L 31/0693"],
    },
    {
        "code": "H01M 8/18",
        "name": "Redox Flow Batteries",
        "description": "Electrochemical energy storage systems using liquid electrolytes circulated through electrochemical cells.",
        "subclasses": ["H01M 8/184", "H01M 8/188"],
    },
    {
        "code": "H04B 7/06",
        "name": "Antenna Systems — Beamforming",
        "description": "Antenna arrays with electronic beam steering for wireless communication including MIMO and massive MIMO.",
        "subclasses": ["H04B 7/0617", "H04B 7/0626"],
    },
    {
        "code": "H04L 12/723",
        "name": "Network Routing and Switching",
        "description": "Methods and apparatus for routing and switching data packets in communication networks.",
        "subclasses": ["H04L 12/7235", "H04L 12/7239"],
    },
    {
        "code": "H04L 41/0893",
        "name": "Network Management — AI-Assisted",
        "description": "Artificial intelligence methods for network configuration, management, and intent translation.",
        "subclasses": ["H04L 41/0896"],
    },
    {
        "code": "C12N 9/22",
        "name": "Nucleases — CRISPR",
        "description": "Engineered nuclease enzymes including CRISPR-Cas systems for genome editing applications.",
        "subclasses": ["C12N 9/222", "C12N 9/228"],
    },
    {
        "code": "C12Q 1/6869",
        "name": "Nucleic Acid Sequencing",
        "description": "Methods and instruments for determining nucleotide sequences including next-generation and long-read sequencing.",
        "subclasses": ["C12Q 1/6874", "C12Q 1/6879"],
    },
    {
        "code": "A61K 47/69",
        "name": "Drug Delivery — Nanoparticles",
        "description": "Pharmaceutical formulations using nanoparticles including lipid nanoparticles for nucleic acid delivery.",
        "subclasses": ["A61K 47/6905", "A61K 47/6911"],
    },
    {
        "code": "B25J 15/00",
        "name": "Robotic Grippers and Manipulators",
        "description": "Robotic end effectors, hands, and gripping devices for automated manipulation tasks.",
        "subclasses": ["B25J 15/02", "B25J 15/08"],
    },
    {
        "code": "B60W 60/00",
        "name": "Autonomous Vehicle Control",
        "description": "Control systems for highly automated and self-driving vehicles including perception and planning.",
        "subclasses": ["B60W 60/001", "B60W 60/0025"],
    },
    {
        "code": "G06F 9/455",
        "name": "Virtual Machines and Containers",
        "description": "Virtualization and containerization technologies for software isolation and resource management.",
        "subclasses": ["G06F 9/4558", "G06F 9/4562"],
    },
    {
        "code": "G06F 16/903",
        "name": "Database Indexing and Search",
        "description": "Index structures and search algorithms for databases including vector and approximate nearest neighbor search.",
        "subclasses": ["G06F 16/9035", "G06F 16/9038"],
    },
    {
        "code": "G06F 21/57",
        "name": "Trusted Computing and Attestation",
        "description": "Hardware security features including trusted execution environments, secure boot, and remote attestation.",
        "subclasses": ["G06F 21/572", "G06F 21/575"],
    },
    {
        "code": "G06N 10/40",
        "name": "Quantum Computing — Hardware",
        "description": "Physical implementations of quantum processors including superconducting, trapped-ion, and photonic systems.",
        "subclasses": ["G06N 10/42", "G06N 10/45"],
    },
    {
        "code": "G06N 10/20",
        "name": "Quantum Computing — Algorithms",
        "description": "Quantum algorithms and variational methods for quantum computing applications.",
        "subclasses": ["G06N 10/22", "G06N 10/25"],
    },
    {
        "code": "H04L 9/40",
        "name": "Network Security — Access Control",
        "description": "Authentication, authorization, and access control mechanisms for network security.",
        "subclasses": ["H04L 9/405", "H04L 9/408"],
    },
    {
        "code": "H04L 9/00",
        "name": "Cryptography",
        "description": "Cryptographic methods and systems including public-key, symmetric, and homomorphic encryption.",
        "subclasses": ["H04L 9/06", "H04L 9/30"],
    },
    {
        "code": "H01L 33/00",
        "name": "Semiconductor Light-Emitting Devices",
        "description": "LEDs, micro-LEDs, and related light-emitting semiconductor devices for display and illumination.",
        "subclasses": ["H01L 33/08", "H01L 33/30"],
    },
    {
        "code": "G02B 27/01",
        "name": "Augmented Reality Optics",
        "description": "Optical systems for augmented and mixed reality displays including waveguides and holographic elements.",
        "subclasses": ["G02B 27/017", "G02B 27/0172"],
    },
    {
        "code": "G16B 15/30",
        "name": "Bioinformatics — Drug Discovery",
        "description": "Computational methods for drug discovery including molecular docking, virtual screening, and QSAR.",
        "subclasses": ["G16B 15/35", "G16B 15/40"],
    },
    {
        "code": "B33Y 10/00",
        "name": "Additive Manufacturing — Processes",
        "description": "Three-dimensional printing processes including FDM, SLA, SLS, and multi-material jetting.",
        "subclasses": ["B33Y 10/005", "B33Y 10/008"],
    },
    {
        "code": "B01J 23/89",
        "name": "Catalysts — Multi-Metal",
        "description": "Heterogeneous catalysts comprising multiple metal components including alloys and high-entropy alloys.",
        "subclasses": ["B01J 23/892", "B01J 23/896"],
    },
    {
        "code": "A01B 79/005",
        "name": "Agriculture — Precision Farming",
        "description": "Precision agriculture systems including GPS-guided equipment, remote sensing, and variable-rate application.",
        "subclasses": ["A01B 79/007"],
    },
    {
        "code": "G06Q 20/40",
        "name": "Payment Systems — Fraud Prevention",
        "description": "Electronic payment systems with fraud detection and prevention mechanisms.",
        "subclasses": ["G06Q 20/401", "G06Q 20/403"],
    },
    {
        "code": "F02K 9/44",
        "name": "Rocket Propulsion — Staged Combustion",
        "description": "Rocket engine cycles including staged combustion, expander, and gas generator cycles.",
        "subclasses": ["F02K 9/445", "F02K 9/448"],
    },
    {
        "code": "H04W 4/38",
        "name": "Wireless Sensor Networks — IoT",
        "description": "Wireless communications for internet of things devices, sensor networks, and machine-type communications.",
        "subclasses": ["H04W 4/382", "H04W 4/385"],
    },
    {
        "code": "G06N 20/00",
        "name": "Machine Learning — General",
        "description": "General machine learning methods including supervised, unsupervised, and semi-supervised learning.",
        "subclasses": ["G06N 20/10", "G06N 20/20"],
    },
]

![](https://raw.githubusercontent.com/insight-decentralized-consensus-lab/monero_quantum_resistance/master/images/dual_logos.png)
# Identifying practical post-quantum strategies for Monero

## Motivation:
Monero transactions created between 2014 and 2020 utilize cryptographic mechanisms that were not designed to be private or secure against quantum computers. Algorithms that could theoretically circumvent several of Monero's security and privacy features are already known, such as [Shor's algorithm](https://ieeexplore.ieee.org/document/365700/) (which [breaks security](https://scialert.net/fulltext/?doi=jas.2005.1692.1712) based on the discrete logarithm problem) and [Grover's algorithm](https://arxiv.org/abs/quant-ph/9605043) (which could be used to [forge blocks](https://www.mitre.org/sites/default/files/publications/17-4039-blockchain-and-quantum-computing.pdf)). 

Let us define a hypothetical “practical” quantum computer as any device that enables an adversary to effectively circumvent some security expectation provided by cryptographic mechanisms. This is not defined by some magic number of qubits or any particular configuration; it refers to the **capability** to leverage methods such as Fourier fishing, Grover's algorithm, or Shor's algorithm with enough complexity to tackle modern cryptography. **Speculation on whether practical quantum computers will ever exist, and when they might arrive, is outside the scope of this cryptography research proposal.**

There are several ways that a sophisticated quantum adversary might access funds and sensitive information that would otherwise be cryptographically obfuscated:

- **Deriving private keys from public keys**: A quantum adversary that has obtained your public wallet address can derive your private key. This enables them to learn your entire (past and subsequent) transaction history, and steal any current/future funds by forging a transaction from you to themselves.
- **Deriving private keys from key images**: A quantum adversary can also break the privacy of some features for every transaction already recorded on the ledger, by using key images to derive transaction private keys.
- **Deobfuscating the transaction graph**: Each ring signature references several (currently 11) past outputs, only one of which is truly being spent. Deobfuscation refers to analyzing the true flow of funds to eliminate the privacy provided by ring signatures and stealth addresses. Graph matching analyses are already parallelizable on traditional computers, and may be easier for quantum computers.
- **Consensus mechanism & blockchain immutability**: Monero's proof-of-work algorithm ([RandomX](https://github.com/tevador/RandomX)) involves chaining several (currently 8) operations by a VM, designed like a one way function (such that the input to produce a given output can only be found by brute force). We will evaluate whether this approach can be exploited by quantum computers leveraging methods such as Fourier fishing or Grover's algorithm. The potential ability to forge blocks with a specific hash would defeat blockchain immutability, however this can be mitigated with the addition (i.e. concatenation) of post-quantum hash functions and checksums.

**Retroactive deanonymization puts today's Monero users at the hands of tomorrow's [quantum or classical] adversaries.** If practical quantum computers that can break Monero's encryption arrive at any point in the future, then users' lifelong transaction history willl become public for ingestion by the AdTech industry, stalkers, criminals, and governments. It is irrelevant which party publishes a de-anonymized copy of the Monero blockchain first - the universal evaporation of privacy is irreversible.

Thankfully, cryptographers have developed several post-quantum security and privacy schemes that may be adaptable to Monero. Promising techniques include [zero-knowledge lattice cryptography](https://eprint.iacr.org/2019/747.pdf)  based on the [shortest vector problem](https://en.wikipedia.org/wiki/Lattice_problem#Shortest_vector_problem_(SVP)). Methods such as [hash-based ring signatures](https://eprint.iacr.org/2019/567.pdf), [GLYPH](https://eprint.iacr.org/2017/766.pdf) (Schnorr-like lattice-based signature scheme), and the cohort of [NIST post-quantum](https://csrc.nist.gov/news/2019/pqc-standardization-process-2nd-round-candidates) candidates were all designed to enable security in a post-quantum world. Applications to [anonymous post-quantum cryptocash](https://eprint.iacr.org/2017/716.pdf) have been considered, and the [Halo](https://eprint.iacr.org/2019/1021.pdf) recursive zero-knowledge proving system offers plausible post-quantum security. Each approach has its own benefits, drawbacks, and space/time complexity - our research recommendations will take into account these practical considerations in addition to theoretical compatibility.

**This research will (1) study and simulate the threats listed above to assess vulnerability to quantum computers, (2) evaluate post-quantum cryptography scheme candidates to create a roadmap for hardening Monero against quantum adversaries, and (3) provide open-source proof-of-concept code and demos where applicable.**

The advent of powerful quantum computers will wreak havoc on almost every aspect of our digital infrastructure. Access to sound money (which requires privacy) is a fundamental human right and should be considered a high priority for hardening against quantum adversaries. To our knowledge, there are currently no plausibly post-quantum anonymous currencies in use today, meaning that only short-to-intermediate term financial privacy is available with current technology. The first coin to implement long-term post-quantum privacy features will be in a strong position for adoption, even long before quantum computers arrive.

>"A post-quantum world would destroy Amazon, Wells Fargo, Visa, and most world governments. But there's no reason it has to also destroy Monero." 
>
> _Surae Noether_

## Overview:

R &amp; D Institution: Insight

Funding Institution: Monero CCS

Duration: 3 months (June - August 2020)

Contributors:

- Researcher in Residence: Adam Corbo
  - Decentralized Consensus Fellow at Insight
  - Developed open-source proof-of-concept quantum PoW miner
  - Expertise translating academic/mathematics research into code 
  - 2 years of experience in quantum information theory and computation at UC Berkeley
  - [GitHub](https://github.com/hamburgerguy/), [Twitter](https://twitter.com/adamryancorbo/), [LinkedIn](https://www.linkedin.com/in/adam-corbo/)
- Principal Investigator: Mitchell Krawiec-Thayer
  - Head of Research, Developers in Residence at [Insight](http://www.insightconsensus.com/)
  - Data Science for Monero Research Lab
  - Quantum classes &amp; calculations during PhD (in context of spectroscopy research)
  - [GitHub](https://github.com/mitchellpkt/), [Twitter](https://twitter.com/Mitchellpkt0), [LinkedIn](https://www.linkedin.com/in/mitchellpkt/), [Medium](https://medium.com/@mitchellpkt)
- Other Insight contributors
  - Code &amp; documentation reviewers will be assigned as milestones near completion.
  - Additional thanks to office staff, accounting, etc for creating a productive workspace.

## Project Roadmap:

### Phase 1: Identify and document existing vulnerabilities in Monero

The first phase of this problem will focus on identifying which of Monero's security features are susceptible to quantum adversaries. We'll look for vulnerabilities to known tools such as Shor's algorithm (which can find discrete logarithms is polynomial time, breaking the DL problem), Grover's algorithm (which produces a quadratic speedup when searching for inputs that map to a particular output for any black box function), and Fourier fishing in conjunction with the Deutsch-Josza algorithm (which can potentially be used in taking advantage of Monero's proof of work method in bounded-error quantum polynomial time).

Some vulnerabilities are already known, for example that cryptography based on elliptic curve and the discrete logarithm problem can be made insecure using Shor's algorithm. We will examine Monero's protocol for other examples of security based on problems that are computationally intractable for classical computers and easy for quantum computers. Some current privacy features are thought to be quantum resistant (such as Monero's masked amounts) and we will cautiously verify their security against our algorithmic adversarial toolkit.

**Phase 1 deliverables:** 

-  Formally enumerate adversary model capabilities: Shor's algorithm, Grover's algorithm, Fourier fishing, etc.
-  Enumerate Monero mechanisms of interest: ring signatures, bulletproofs, stealth addresses, asymmetric cryptography, consensus mechanism, etc.
-  Systematically assess the impacts of each algorithm on each mechanism, completing this table: 

|                     | Monero mechanism 1 | Monero mechanism 2 | ... |
|---------------------|--------------------|--------------------|-----|
|  Shor's algorithm   |  Plausibly secure  | Plausibly secure   | ... |
|  Grover's algorithm | Irrelevant         | **VULNERABLE** | ... |
| Fourier Fishsing    | Plausibly secure   | Irrelevant         | ... |
| ...                 | ...                | ...                | ... |

### Phase 2: Research Monero-compatible post-quantum cryptography methods

After locating and documenting Monero's quantum vulnerabilities, we will identify alternative cryptographic schemes that mitigate these weaknesses. Known post-quantum systems will be examined for Monero-compatibility (see Appendix 1 for a list of potentially relevant literature to be analyzed). In addition to interoperability, we will note practical considerations related to verification time, signature/proof size, and implementation. If there are no known solutions for mitigating a particular vulnerability, we will note the constraints necessary for developing a unique solution.

There are three broad categories of implications, which are not mutually exclusive:

- Deanonymization (knowing more about others' transactions than you should)
- Theft (being able to move others' funds)
- Mining speedup (obtaining valid nonces paradigmatically faster)

Vulnerable privacy features will be given highest priority, since retroactive deanonymization poses a threat to today's Monero users, whereas theft and mining are not an issue until quantum computers scale past a distant threshold. Mining vulnerabilities are the lowest priority, since switching consensus mechanisms is easier than implementing new cryptographic schemes. 

It's important to note that many current post-quantum cryptography candidates require large proofs and significant computational resources, and will thus not be suitable for immediate deployment. For this reason, understanding broad strategies and their tradeoff will be more useful than specific implementations. Thankfully, consumer device capabilities increase over time, and researchers continue to discover new faster/smaller proving systems, so these practical barriers are temporary. 

**Phase 2 deliverables:** List of vulnerabilities, following this format when possible:

> Monero's **[component]** is vulnerable to **[impact]** by a hypothetical adversary that can leverage **[algorithm]**. In general, the solution must meet **[requirements]**. Current relevant methods include **[cryptosystem]** which would require **[migration process]** and has **[tradeoffs]** that would prevent implementation until **[bandwidth/power threshold]** is widely available.

### Phase 3: Communicate and Educate

Throughout this entire project, the community will receive updates during the weekly #monero-research-lab meetings. During phase 3 however, several specific documents (the key deliverables from this research) will be freely published: 

**Phase 3 deliverables:** 

1. **User-friendly writeup:** This community-facing writeup will provide an approachable explanation of how hypothetical quantum computers may impact Monero, and possible future mitigations. The writeup should minimize FUD and provide the context that these vulnerabilities apply to almost all cryptocurrencies (not only Monero).

2. **Technical documentation:** An MRL position paper to distill key information for (current and future) researchers and developers. The writeup should formally describe vulnerabilities, and highlight potential strategies and solutions, noting their tradeoffs. Code snippets may be included if appropriate for pedagogical purposes or clarity.

3. **Non-technical 1-pager:** An ELI5 / TL;DR summary will be provided for journalists, Monero Outreach, etc. This blurb will discuss risks and myths with no technical jargon, with key takeaways that a broad audience will appreciate.

# Resources

The team tackling this project consists of one full-time researcher dedicated solely to this proposal (Adam), along with mentoring and writing by Mitchell (5-15 hr/wk), input from the Director of Security, and internal editors/reviewers. We intend to execute this research initiative over a twelve week period between June - August 2020 for 37500 USD.

Insight's bills and employees' salaries are dollar-denominated, so we must minimize exposure to volatility risk. We are open to three different approaches, and will let the community choose how to proceed:

1. If payouts can only be received after the work is completed, we will need to add a volatility buffer (see [TL;DR explanation](https://twitter.com/Mitchellpkt0/status/1252720219644063745), and [open source code](https://github.com/Mitchellpkt/volatility_analysis/blob/master/volatility_analysis.ipynb)). Based on the last 2 years of data, and a 4-month window (1 month of fundraising + 3 months of reseearch), a 35% buffer provides a 80% statistical confidence of receiving sufficient payout. Thus the CCS goal would include an extra 4375 USD per month
2. If the funds can be released at the beginning of the research period, then no buffer is necessary.
3. Some mutually-trusted third party could escrow the funds in fiat form (to eliminate volatility risk), and pay Insight upon satisfactory work.

# Appendix 1 - Literature

Here is relevant literature that will be reviewed and annotated for utility to Monero. List compiled by Dr. Brandon Gooddell

- Liu, Joseph K., Victor K. Wei, and Duncan S. Wong. 'Linkable spontaneous anonymous group signature for ad hoc groups.' Australasian Conference on Information Security and Privacy. Springer, Berlin, Heidelberg, 2004.
- Zhang, Huang, et al. 'Anonymous post-quantum cryptocash.' International Conference on Financial Cryptography and Data Security. Springer, Berlin, Heidelberg, 2018.
- Torres, Wilson Abel Alberto, et al. 'Post-quantum one-time linkable ring signature and application to ring confidential transactions in blockchain (lattice RingCT v1. 0).' Australasian Conference on Information Security and Privacy. Springer, Cham, 2018.
- Groth, Jens, and Markulf Kohlweiss. 'One-out-of-many proofs: Or how to leak a secret and spend a coin.' Annual International Conference on the Theory and Applications of Cryptographic Techniques. Springer, Berlin, Heidelberg, 2015.
- Chopra, Arjun. 'GLYPH: A New Instantiation of the GLP Digital Signature Scheme.' IACR Cryptology ePrint Archive 2017 (2017): 766.
- Unruh, Dominique. 'Post-quantum security of Fiat-Shamir.' International Conference on the Theory and Application of Cryptology and Information Security. Springer, Cham, 2017.
- Okamoto, Tatsuaki, et al. 'New realizations of somewhere statistically binding hashing and positional accumulators.' International Conference on the Theory and Application of Cryptology and Information Security. Springer, Berlin, Heidelberg, 2015.
- Lu, Xingye, Man Ho Au, and Zhenfei Zhang. '(Linkable) Ring Signature from Hash-Then-One-Way Signature.' 2019 18th IEEE International Conference On Trust, Security And Privacy In Computing And Communications/13th IEEE International Conference On Big Data Science And Engineering (TrustCom/BigDataSE). IEEE, 2019.
- Backes, Michael, et al. 'Ring signatures: Logarithmic-size, no setup—from standard assumptions.' Annual International Conference on the Theory and Applications of Cryptographic Techniques. Springer, Cham, 2019.
- Yang, Rupeng, et al. 'Efficient lattice-based zero-knowledge arguments with standard soundness: construction and applications.' Annual International Cryptology Conference. Springer, Cham, 2019.
- Esgin, Muhammed F., et al. 'MatRiCT: Efficient, Scalable and Post-Quantum Blockchain Confidential Transactions Protocol.' Proceedings of the 2019 ACM SIGSAC Conference on Computer and Communications Security. 2019.
- Torres, Wilson Alberto, et al. 'Lattice RingCT v2. 0 with Multiple Input and Multiple Output Wallets.' Australasian Conference on Information Security and Privacy. Springer, Cham, 2019.
- Ruffing, Tim, and Giulio Malavolta. 'Switch commitments: A safety switch for confidential transactions.' International Conference on Financial Cryptography and Data Security. Springer, Cham, 2017.
- Zhang, Huang, et al. 'Anonymous post-quantum cryptocash.' International Conference on Financial Cryptography and Data Security. Springer, Berlin, Heidelberg, 2018.
- Zhang, Huang, et al. 'Implementing confidential transactions with lattice techniques.' IET Information Security 14.1 (2019): 30-38.
- [http://www.fields.utoronto.ca/talks/Toward-More-Secure-Quantum-Future](http://www.fields.utoronto.ca/talks/Toward-More-Secure-Quantum-Future)

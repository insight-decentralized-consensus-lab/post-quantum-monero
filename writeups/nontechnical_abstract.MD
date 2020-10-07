All research deliverables:
- [Non-technical abstract](https://github.com/insight-decentralized-consensus-lab/post-quantum-monero/blob/master/writeups/nontechnical_abstract.MD) (this document)
- [Semi-technical summary](https://github.com/insight-decentralized-consensus-lab/post-quantum-monero/blob/master/writeups/semitechnical_summary.MD)
- [Technical note](https://github.com/insight-decentralized-consensus-lab/post-quantum-monero/blob/master/writeups/technical_note.pdf)

![https://raw.githubusercontent.com/insight-decentralized-consensus-lab/post-quantum-monero/master/images/dual_logos.png](https://raw.githubusercontent.com/insight-decentralized-consensus-lab/post-quantum-monero/master/images/dual_logos.png)

## Evaluating cryptocurrency security in a quantum context (non-technical abstract)

_September 2020_

Insight recently completed an examination of Monero’s cryptographic mechanisms in the context of several well-known quantum computing algorithms. The cryptographic underpinnings of essentially all cryptocurrencies (e.g. Bitcoin, Ethereum, Monero, Zcash, etc) are based on the fact that certain types of mathematical problems are effectively impossible for classical computers to solve. However, several algorithms are known to make these calculations easier for quantum computers, compromising security based on assumptions that those problems are hard.

Our biggest concern is the fact that a quantum computer could extract a wallet’s seed from its public address, due to a vulnerability that affects essentially every cryptocurrency in use today. Another significant concern is the fact that a quantum adversary could potentially tamper with transaction amounts to forge Monero, however we suggest an efficient mitigation with a known solution. The “ring signature” feature designed to provide sender anonymity is not robust against a quantum adversary, however quantum-secure ring signatures have been developed and could be implemented.

Thankfully, post-quantum cryptography has been extensively studied, and we found several schemes to which Monero can be eventually adapted. We identify and describe several promising replacements that offer post-quantum security and privacy with minimal drawbacks, and we note some tradeoffs required for implementation.

Given that the problems we describe are fundamental concerns for essentially every cryptocurrency, we hope that our research provides a starting point and inspiration for other ecosystems to examine their own cryptographic mechanisms in the context of quantum computers.

Contributors: Adam Corbo, Mitchell “Isthmus” Krawiec-Thayer, and Brandon G. Goodell

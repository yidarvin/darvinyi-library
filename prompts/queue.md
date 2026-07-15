# Run Queue --- the library

Run order, top to bottom. The **next** item is the first `PENDING` row. Statuses:
`PENDING`, `DONE`, `SKIPPED`. Update the status cell after each run. Reorder by
moving rows. Adding a book means adding a `PENDING` row here and a matching entry
in `content/registry.json` (or just add it to `prompts/_books.py` and re-run
`python3 prompts/_generate.py`). See `AGENTS.md` and the `library-runner` skill for
the per-item procedure. A built page becomes `DONE` only after an independent critique.

The first row, `about`, is the bootstrap: building it also builds the library
landing page, the diagram primitive components, and the shared book-page layout.
Run it first. Every row after it is one book. Each book has a brief at
`prompts/notes/<slug>.md`.

| #   | slug                            | item                                          | status  |
|-----|---------------------------------|-----------------------------------------------|---------|
| 000 | about                           | About this library                            | DONE    |
| 001 | atomic-habits                   | Atomic Habits                                 | DONE    |
| 002 | thinking-fast-and-slow          | Thinking, Fast and Slow                       | DONE    |
| 003 | seven-habits                    | The 7 Habits of Highly Effective People       | DONE    |
| 004 | how-to-win-friends              | How to Win Friends and Influence People       | DONE    |
| 005 | sapiens                         | Sapiens                                       | DONE    |
| 006 | mans-search-for-meaning         | Man's Search for Meaning                      | DONE    |
| 007 | psychology-of-money             | The Psychology of Money                       | DONE    |
| 008 | start-with-why                  | Start With Why                                | PENDING |
| 009 | mindset                         | Mindset                                       | PENDING |
| 010 | influence                       | Influence: The Psychology of Persuasion       | PENDING |
| 011 | power-of-habit                  | The Power of Habit                            | PENDING |
| 012 | rich-dad-poor-dad               | Rich Dad Poor Dad                             | PENDING |
| 013 | deep-work                       | Deep Work                                     | PENDING |
| 014 | never-split-the-difference      | Never Split the Difference                    | PENDING |
| 015 | subtle-art                      | The Subtle Art of Not Giving a F*ck           | PENDING |
| 016 | predictably-irrational          | Predictably Irrational                        | PENDING |
| 017 | nudge                           | Nudge                                         | PENDING |
| 018 | black-swan                      | The Black Swan                                | PENDING |
| 019 | intelligent-investor            | The Intelligent Investor                      | PENDING |
| 020 | freakonomics                    | Freakonomics                                  | PENDING |
| 021 | good-to-great                   | Good to Great                                 | PENDING |
| 022 | lean-startup                    | The Lean Startup                              | PENDING |
| 023 | zero-to-one                     | Zero to One                                   | PENDING |
| 024 | drive                           | Drive                                         | PENDING |
| 025 | innovators-dilemma              | The Innovator's Dilemma                       | PENDING |
| 026 | nonviolent-communication        | Nonviolent Communication                      | PENDING |
| 027 | crucial-conversations           | Crucial Conversations                         | PENDING |
| 028 | five-love-languages             | The 5 Love Languages                          | PENDING |
| 029 | getting-to-yes                  | Getting to Yes                                | PENDING |
| 030 | emotional-intelligence          | Emotional Intelligence                        | PENDING |
| 031 | grit                            | Grit                                          | PENDING |
| 032 | body-keeps-the-score            | The Body Keeps the Score                      | PENDING |
| 033 | guns-germs-steel                | Guns, Germs, and Steel                        | PENDING |
| 034 | outliers                        | Outliers                                      | PENDING |
| 035 | selfish-gene                    | The Selfish Gene                              | PENDING |
| 036 | short-history-nearly-everything | A Short History of Nearly Everything          | PENDING |
| 037 | thinking-in-systems             | Thinking in Systems                           | PENDING |
| 038 | range                           | Range                                         | PENDING |
| 039 | meditations                     | Meditations                                   | PENDING |
| 040 | obstacle-is-the-way             | The Obstacle Is the Way                       | PENDING |
| 041 | power-of-now                    | The Power of Now                              | PENDING |
| 042 | peak                            | Peak                                          | PENDING |
| 043 | big-magic                       | Big Magic                                     | PENDING |
| 044 | steal-like-an-artist            | Steal Like an Artist                          | PENDING |
| 045 | on-writing                      | On Writing                                    | PENDING |
| 046 | why-we-sleep                    | Why We Sleep                                  | PENDING |
| 047 | superforecasting                | Superforecasting                              | PENDING |
| 048 | thinking-in-bets                | Thinking in Bets                              | PENDING |
| 049 | fooled-by-randomness            | Fooled by Randomness                          | PENDING |
| 050 | paradox-of-choice               | The Paradox of Choice                         | PENDING |
| 051 | blink                           | Blink                                         | PENDING |
| 052 | getting-things-done             | Getting Things Done                           | PENDING |
| 053 | essentialism                    | Essentialism                                  | PENDING |
| 054 | flow                            | Flow                                          | PENDING |
| 055 | the-one-thing                   | The One Thing                                 | PENDING |
| 056 | four-thousand-weeks             | Four Thousand Weeks                           | PENDING |
| 057 | almanack-naval                  | The Almanack of Naval Ravikant                | PENDING |
| 058 | think-and-grow-rich             | Think and Grow Rich                           | PENDING |
| 059 | random-walk                     | A Random Walk Down Wall Street                | PENDING |
| 060 | millionaire-next-door           | The Millionaire Next Door                     | PENDING |
| 061 | richest-man-babylon             | The Richest Man in Babylon                    | PENDING |
| 062 | common-sense-investing          | The Little Book of Common Sense Investing     | PENDING |
| 063 | dare-to-lead                    | Dare to Lead                                  | PENDING |
| 064 | built-to-last                   | Built to Last                                 | PENDING |
| 065 | good-strategy                   | Good Strategy Bad Strategy                    | PENDING |
| 066 | hard-thing                      | The Hard Thing About Hard Things              | PENDING |
| 067 | blue-ocean                      | Blue Ocean Strategy                           | PENDING |
| 068 | e-myth                          | The E-Myth Revisited                          | PENDING |
| 069 | extreme-ownership               | Extreme Ownership                             | PENDING |
| 070 | four-hour-workweek              | The 4-Hour Workweek                           | PENDING |
| 071 | effective-executive             | The Effective Executive                       | PENDING |
| 072 | difficult-conversations         | Difficult Conversations                       | PENDING |
| 073 | seven-principles-marriage       | The Seven Principles for Making Marriage Work | PENDING |
| 074 | made-to-stick                   | Made to Stick                                 | PENDING |
| 075 | quiet                           | Quiet                                         | PENDING |
| 076 | happiness-hypothesis            | The Happiness Hypothesis                      | PENDING |
| 077 | flourish                        | Flourish                                      | PENDING |
| 078 | four-agreements                 | The Four Agreements                           | PENDING |
| 079 | twelve-rules                    | 12 Rules for Life                             | PENDING |
| 080 | feeling-good                    | Feeling Good                                  | PENDING |
| 081 | homo-deus                       | Homo Deus                                     | PENDING |
| 082 | cosmos                          | Cosmos                                        | PENDING |
| 083 | brief-history-time              | A Brief History of Time                       | PENDING |
| 084 | the-gene                        | The Gene                                      | PENDING |
| 085 | why-nations-fail                | Why Nations Fail                              | PENDING |
| 086 | factfulness                     | Factfulness                                   | PENDING |
| 087 | emperor-maladies                | The Emperor of All Maladies                   | PENDING |
| 088 | henrietta-lacks                 | The Immortal Life of Henrietta Lacks          | PENDING |
| 089 | antifragile                     | Antifragile                                   | PENDING |
| 090 | fifth-discipline                | The Fifth Discipline                          | PENDING |
| 091 | daily-stoic                     | The Daily Stoic                               | PENDING |
| 092 | tao-te-ching                    | Tao Te Ching                                  | PENDING |
| 093 | letters-from-a-stoic            | Letters from a Stoic                          | PENDING |
| 094 | ego-is-the-enemy                | Ego Is the Enemy                              | PENDING |
| 095 | untethered-soul                 | The Untethered Soul                           | PENDING |
| 096 | wherever-you-go                 | Wherever You Go, There You Are                | PENDING |
| 097 | make-it-stick                   | Make It Stick                                 | PENDING |
| 098 | ultralearning                   | Ultralearning                                 | PENDING |
| 099 | bird-by-bird                    | Bird by Bird                                  | PENDING |
| 100 | war-of-art                      | The War of Art                                | PENDING |
| 101 | artists-way                     | The Artist's Way                              | PENDING |
| 102 | breath                          | Breath                                        | PENDING |
| 103 | outlive                         | Outlive                                       | PENDING |
| 104 | misbehaving                     | Misbehaving                                   | PENDING |
| 105 | stumbling-on-happiness          | Stumbling on Happiness                        | PENDING |
| 106 | noise                           | Noise                                         | PENDING |
| 107 | make-time                       | Make Time                                     | PENDING |
| 108 | indistractable                  | Indistractable                                | PENDING |
| 109 | your-money-or-your-life         | Your Money or Your Life                       | PENDING |
| 110 | i-will-teach-you                | I Will Teach You to Be Rich                   | PENDING |
| 111 | capital-21c                     | Capital in the Twenty-First Century           | PENDING |
| 112 | total-money-makeover            | The Total Money Makeover                      | PENDING |
| 113 | measure-what-matters            | Measure What Matters                          | PENDING |
| 114 | 48-laws-of-power                | The 48 Laws of Power                          | PENDING |
| 115 | originals                       | Originals                                     | PENDING |
| 116 | radical-candor                  | Radical Candor                                | PENDING |
| 117 | culture-code                    | The Culture Code                              | PENDING |
| 118 | talking-to-strangers            | Talking to Strangers                          | PENDING |
| 119 | supercommunicators              | Supercommunicators                            | PENDING |
| 120 | attached                        | Attached                                      | PENDING |
| 121 | getting-past-no                 | Getting Past No                               | PENDING |
| 122 | bargaining-for-advantage        | Bargaining for Advantage                      | PENDING |
| 123 | talk-to-someone                 | Maybe You Should Talk to Someone              | PENDING |
| 124 | gifts-of-imperfection           | The Gifts of Imperfection                     | PENDING |
| 125 | lost-connections                | Lost Connections                              | PENDING |
| 126 | behave                          | Behave                                        | PENDING |
| 127 | silent-spring                   | Silent Spring                                 | PENDING |
| 128 | sixth-extinction                | The Sixth Extinction                          | PENDING |
| 129 | astrophysics-hurry              | Astrophysics for People in a Hurry            | PENDING |
| 130 | demon-haunted-world             | The Demon-Haunted World                       | PENDING |
| 131 | the-innovators                  | The Innovators                                | PENDING |
| 132 | superintelligence               | Superintelligence                             | PENDING |
| 133 | scientific-revolutions          | The Structure of Scientific Revolutions       | PENDING |
| 134 | godel-escher-bach               | Gödel, Escher, Bach                           | PENDING |
| 135 | guide-to-good-life              | A Guide to the Good Life                      | PENDING |
| 136 | art-of-war                      | The Art of War                                | PENDING |
| 137 | tao-of-pooh                     | The Tao of Pooh                               | PENDING |
| 138 | miracle-of-mindfulness          | The Miracle of Mindfulness                    | PENDING |
| 139 | waking-up                       | Waking Up                                     | PENDING |
| 140 | moonwalking-einstein            | Moonwalking with Einstein                     | PENDING |
| 141 | mind-for-numbers                | A Mind for Numbers                            | PENDING |
| 142 | creative-act                    | The Creative Act                              | PENDING |
| 143 | show-your-work                  | Show Your Work!                               | PENDING |
| 144 | how-not-to-die                  | How Not to Die                                | PENDING |
| 145 | omnivores-dilemma               | The Omnivore's Dilemma                        | PENDING |
| 146 | when-breath-becomes-air         | When Breath Becomes Air                       | PENDING |

<!--
Order is: the launch shelf first (highest-reach Tier 1), then the rest of Tier 1,
then Tier 2, then Tier 3. Within a tier, books are grouped by shelf.

A run reads prompts/notes/<slug>.md for the book's brief (thesis, signature model,
any credibility caveat), then follows docs/authoring-spec.md for the page anatomy
and docs/diagram-vocabulary.md for the diagram forms. validate.py checks that this
table and content/registry.json list the same slugs in the same order, so keep
them in sync (or regenerate both with prompts/_generate.py).
-->

"""
Clark, "Basics of Reinsurance Pricing," explains the concept of loss sensitive features for working layer
excess treaties. One type of loss sensitive program is the "swing plan" retrospective rating program. Suppose a swing
plan works as follows:

- Retro Premium = (Actual Layer Losses) x 1.25
- Provisional Rate = 20% of Subject Premium
- Maximum Premium = 30% of Subject Premium
- Minimum Premium = 15% of Subject Premium
- Subject Premium = $20,000,000

You are given the following distribution of losses:

|Probability|Expected Layer Losses|
===================================
20%         | $1,000,000           |
45%         | $4,000,000           |
35%         | $7,000,000           |
====================================
"""


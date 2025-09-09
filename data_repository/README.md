# Data Repository: Data Labeling Worker Experiences

This repository contains the coded qualitative data and analysis results from a study examining the challenges and improvement suggestions of data labeling workers.

## Citation

If you use this data, please cite:

```
[Your Citation Here - Add when published]
```

## Repository Contents

### Core Data Files
- **`final_manual_coding_NO_Q13.csv`** - RQ1 coded responses (Q7-Q12) with domains, subthemes, and codes
- **`rq2_improvements_only.csv`** - RQ2 coded responses (Q13) with improvement suggestions
- **`codebook.csv`** - Complete coding framework (Domains → Subthemes → Codes with definitions)

### Prevalence Statistics
- **`RQ1_distinct_participants_by_domain.csv`** - Domain prevalence for RQ1 (n and % of 50 participants)
- **`RQ1_distinct_participants_by_subtheme.csv`** - Subtheme prevalence for RQ1 (distinct participants)
- **`rq2_improvements_summary.md`** - Q13 improvement suggestions by domain/subtheme

### Analysis Materials
- **`rq1_quote_shortlist.md`** - Representative quotes by domain (tagged [Pxx, Q#])
- **`mapping_RQ_to_items.csv`** - Research questions mapped to survey items
- **`mapping_domain_to_items.csv`** - Domains mapped to direct and context survey items

### Documentation
- **`questionnaire.pdf`** - Complete survey instrument (Appendix A)
- **`protocol_compliance_summary.md`** - Audit summary and compliance checks
- **`LICENSE`** - Data and code licensing information

## Reproducing Results Tables

### RQ1 Prevalence Tables
1. Load `final_manual_coding_NO_Q13.csv`
2. Count distinct participants by domain: `groupby('Domain')['PID'].nunique()`
3. Count distinct participants by subtheme: `groupby('Subtheme')['PID'].nunique()`
4. Results are provided in `RQ1_distinct_participants_by_domain.csv` and `RQ1_distinct_participants_by_subtheme.csv`

### RQ2 Improvement Analysis
1. Load `rq2_improvements_only.csv`
2. Count distinct participants by domain: `groupby('Domain')['PID'].nunique()`
3. Count distinct participants by subtheme: `groupby('Subtheme')['PID'].nunique()`
4. Results are provided in `rq2_improvements_summary.md`

### Quote Selection
- Representative quotes are provided in `rq1_quote_shortlist.md`
- Quotes are tagged with participant ID and question number [Pxx, Q#]
- One quote per participant per domain to avoid overweighting

## Data Structure

### Coding Framework
- **6 Domains**: Compensation & Economic Security, Task Design & Time Pressure, Transparency & QA, Content Exposure & Emotional Load, Platform Reliability & Access, Support & Dispute Resolution
- **Subthemes**: Inductive groupings within each domain
- **Codes**: Specific labels applied to text segments (≤5 codes per response)

### Sample Sizes
- **Total Participants**: 50
- **RQ1 Responses**: 206 (Q7-Q12)
- **RQ2 Responses**: 50 (Q13)
- **Response Rate**: 100% for all questions

## Quality Assurance

- **Coding Calibration**: Initial coding on 20% of responses with reconciliation
- **Routing Rules**: Clear domain assignment rules based on content type
- **Code Limits**: Maximum 5 codes per response to maintain focus
- **Audit Trail**: All quotes tagged with participant and question identifiers

## Contact

For questions about this data or analysis, please contact [Your Contact Information].

## License

- **Data**: CC BY 4.0 (Creative Commons Attribution 4.0 International)
- **Code**: MIT License


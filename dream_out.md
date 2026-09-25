# dream.py output, 25 Sep 2026

Manual schedule_dream on the managed tier, 150s wait, then representation, card, and one high-level chat with evidence. Raw output follows; the EV conclusions line is the SDK object repr.

```
SCHEDULE: None
REP: ## Explicit Observations

[2026-09-25 03:19:56] maya's manager wants her to present at the offsite next month.
[2026-09-25 03:19:56] maya settled in Chicago now.
[2026-09-25 03:19:56] maya finds the Lakefront path in Chicago not bad actually.
[2026-09-25 03:19:56] maya is more comfortable in the lab than on stage.
[2026-09-25 03:19:56] maya is moving to Chicago next week.
[2026-09-25 03:19:56] maya took a role at a hospital system in Chicago.

## Deductive Observations

[2026-09-25 03:19:56] maya is a regular runner (roughly 5k most mornings), and her habitual running route changed from Boston's Charles River to Chicago's Lakefront path.
   Premises:
   - maya runs along the Charles most mornings, usually 5k.
   - maya finds the Lakefront path in Chicago not bad actually.
   - maya settled in Chicago now.

[2026-09-25 03:19:56] maya works in a hands-on/life-sciences role centered on lab work rather than public speaking, given her preference for the lab over the stage.
   Premises:
   - maya is more comfortable in the lab than on stage.
   - maya just moved to Boston for a new job at a biotech startup.

[2026-09-25 03:19:56] maya is an employee with a manager who sets expectations for her, including presenting at a company offsite.
   Premises:
   - maya's manager wants her to present at the offsite next month.
   - maya is more comfortable in the lab than on stage.

[2026-09-25 03:19:56] maya's current location and job supersede her Boston situation: she relocated from Boston to Chicago, taking a role at a hospital system there and is now settled in Chicago.
   Premises:
   - maya just moved to Boston for a new job at a biotech startup.
   - maya took a role at a hospital system in Chicago.
   - maya settled in Chicago now.

[2026-09-25 03:19:56] maya changed employers: from a biotech startup (Boston) to a hospital system (Chicago).
   Premises:
   - maya just moved to Boston for a new job at a biotech startup.
   - maya took a role at a hospital system in Chicago.


## Inductive Observations

 **Pattern** [medium]: Maya adapts to disruptive transitions with an understated, mildly optimistic attitude — reframing a new city's running path as 'not bad actually' and settling in after an initial sense of loss.
   **Type**: tendency
   **Sources**:
   - maya finds the Lakefront path in Chicago not bad actually.
   - maya settled in Chicago now.
   - maya relocated from Boston to Chicago, taking a role at a hospital system there and is now settled in Chicago.

 **Pattern** [low]: Maya maintains a consistent morning running routine (roughly 5k) and adjusts her route to fit each new city, shifting from Boston's Charles River to Chicago's Lakefront path.
   **Type**: behavior
   **Sources**:
   - maya is a regular runner (roughly 5k most mornings), and her habitual running route changed from Boston's Charles River to Chicago's Lakefront path.
   - maya finds the Lakefront path in Chicago not bad actually.

 **Pattern** [medium]: Maya prefers hands-on life-sciences/lab work over public-facing activities, being more comfortable in the lab than on stage and describing presenting as something she dreads.
   **Type**: preference
   **Sources**:
   - maya is more comfortable in the lab than on stage.
   - maya works in a hands-on/life-sciences role centered on lab work rather than public speaking.
   - maya is an employee with a manager who sets expectations for her, including presenting at a company offsite.

 **Pattern** [high]: Maya makes major life changes in rapid succession — she relocated to Boston for a biotech startup role and then quickly took a role at a hospital system in Chicago, moving cities and changing employers within a short span.
   **Type**: behavior
   **Sources**:
   - maya is moving to Chicago next week.
   - maya took a role at a hospital system in Chicago.
   - maya relocated from Boston to Chicago, taking a role at a hospital system there and is now settled in Chicago.
   - maya changed employers: from a biotech startup (Boston) to a hospital system (Chicago).


CARD: ['IDENTITY: Name: maya', 'ATTRIBUTE: Location: Chicago', 'ATTRIBUTE: Employer: a hospital system in Chicago', 'ATTRIBUTE: Works in a lab-based life-sciences role']
ANS: 

Maya currently lives in Chicago.
EV conclusions: [EvidenceObservation(id='0-OUAxisUIp0iguiieufm', level='inductive', content='Maya makes major life changes in rapid succession — she relocated to Boston for a biotech startup role and then quickly took a role at a hospital system in Chicago, moving cities and changing employers within a short span.', created_at=datetime.datetime(2026, 9, 25, 3, 19, 56, tzinfo=TzInfo(0)), session_id=None, observer_id='maya', observed_id='maya', source_ids=['x-tLd0Cn2ZlK85MCJoje8', 'wgDiK3Ph50XOdFmyKOi3c', 'pILIkc5Z09zmb3MqAYZa_', 'EEi1jvAp0C_YYOr0Dm8r1']), EvidenceObservation(id='4L4ARAk5MQjuYj6qmthaA', level='inductive', content='Maya prefers hands-on life-sciences/lab work over public-facing activities, being more comfortable in the lab than on stage and describing presenting as something she dreads.', created_at=datetime.datetime(2026, 9, 25, 3, 19, 56, tzinfo=TzInfo(0)), session_id=None, observer_id='maya', observed_id='maya', source_ids=['yFk61K1l-r2gfWVhR5Qac', 'xx8kJdJLLh90cuTc0TN_1', '8Hysr82pxGWtOjVFbrx6o']), EvidenceObservation(id='8Hysr82pxGWtOjVFbrx6o', level='deductive', content='maya is an employee with a manager who sets expectations for her, including presenting at a company offsite.', created_at=datetime.datetime(2026, 9, 25, 3, 19, 56, tzinfo=TzInfo(0)), session_id=None, observer_id='maya', observed_id='maya', source_ids=['D3wP36gqK9A_P7OJbS-4T', 'yFk61K1l-r2gfWVhR5Qac']), EvidenceObservation(id='D3wP36gqK9A_P7OJbS-4T', level='explicit', content="maya's manager wants her to present at the offsite next month.", created_at=datetime.datetime(2026, 9, 25, 3, 19, 56, tzinfo=TzInfo(0)), session_id='probe-1', observer_id='maya', observed_id='maya', source_ids=[]), EvidenceObservation(id='EEi1jvAp0C_YYOr0Dm8r1', level='deductive', content='maya changed employers: from a biotech startup (Boston) to a hospital system (Chicago).', created_at=datetime.datetime(2026, 9, 25, 3, 19, 56, tzinfo=TzInfo(0)), session_id=None, observer_id='maya', observed_id='maya', source_ids=['HW0t2YOmNZj5tpn0m4tUO', 'wgDiK3Ph50XOdFmyKOi3c']), EvidenceObservation(id='TvXjHTXVajfWRdyPU91g1', level='inductive', content="Maya maintains a consistent morning running routine (roughly 5k) and adjusts her route to fit each new city, shifting from Boston's Charles River to Chicago's Lakefront path.", created_at=datetime.datetime(2026, 9, 25, 3, 19, 56, tzinfo=TzInfo(0)), session_id=None, observer_id='maya', observed_id='maya', source_ids=['zCdrk4XXZ3mwym-7GB-jJ', 'aXSriaH1DnQ1EaLD1TVDc']), EvidenceObservation(id='aXSriaH1DnQ1EaLD1TVDc', level='explicit', content='maya finds the Lakefront path in Chicago not bad actually.', created_at=datetime.datetime(2026, 9, 25, 3, 19, 56, tzinfo=TzInfo(0)), session_id='probe-1', observer_id='maya', observed_id='maya', source_ids=[]), EvidenceObservation(id='evBcF9iP_wAcikAvkrM0f', level='inductive', content="Maya adapts to disruptive transitions with an understated, mildly optimistic attitude — reframing a new city's running path as 'not bad actually' and settling in after an initial sense of loss.", created_at=datetime.datetime(2026, 9, 25, 3, 19, 56, tzinfo=TzInfo(0)), session_id=None, observer_id='maya', observed_id='maya', source_ids=['aXSriaH1DnQ1EaLD1TVDc', 'jv22v7VqR0n3e2xFLmemU', 'pILIkc5Z09zmb3MqAYZa_']), EvidenceObservation(id='jv22v7VqR0n3e2xFLmemU', level='explicit', content='maya settled in Chicago now.', created_at=datetime.datetime(2026, 9, 25, 3, 19, 56, tzinfo=TzInfo(0)), session_id='probe-1', observer_id='maya', observed_id='maya', source_ids=[]), EvidenceObservation(id='pILIkc5Z09zmb3MqAYZa_', level='deductive', content="maya's current location and job supersede her Boston situation: she relocated from Boston to Chicago, taking a role at a hospital system there and is now settled in Chicago.", created_at=datetime.datetime(2026, 9, 25, 3, 19, 56, tzinfo=TzInfo(0)), session_id=None, observer_id='maya', observed_id='maya', source_ids=['HW0t2YOmNZj5tpn0m4tUO', 'wgDiK3Ph50XOdFmyKOi3c', 'jv22v7VqR0n3e2xFLmemU']), EvidenceObservation(id='wgDiK3Ph50XOdFmyKOi3c', level='explicit', content='maya took a role at a hospital system in Chicago.', created_at=datetime.datetime(2026, 9, 25, 3, 19, 56, tzinfo=TzInfo(0)), session_id='probe-1', observer_id='maya', observed_id='maya', source_ids=[]), EvidenceObservation(id='x-tLd0Cn2ZlK85MCJoje8', level='explicit', content='maya is moving to Chicago next week.', created_at=datetime.datetime(2026, 9, 25, 3, 19, 56, tzinfo=TzInfo(0)), session_id='probe-1', observer_id='maya', observed_id='maya', source_ids=[]), EvidenceObservation(id='xx8kJdJLLh90cuTc0TN_1', level='deductive', content='maya works in a hands-on/life-sciences role centered on lab work rather than public speaking, given her preference for the lab over the stage.', created_at=datetime.datetime(2026, 9, 25, 3, 19, 56, tzinfo=TzInfo(0)), session_id=None, observer_id='maya', observed_id='maya', source_ids=['yFk61K1l-r2gfWVhR5Qac', 'HW0t2YOmNZj5tpn0m4tUO']), EvidenceObservation(id='yFk61K1l-r2gfWVhR5Qac', level='explicit', content='maya is more comfortable in the lab than on stage.', created_at=datetime.datetime(2026, 9, 25, 3, 19, 56, tzinfo=TzInfo(0)), session_id='probe-1', observer_id='maya', observed_id='maya', source_ids=[]), EvidenceObservation(id='zCdrk4XXZ3mwym-7GB-jJ', level='deductive', content="maya is a regular runner (roughly 5k most mornings), and her habitual running route changed from Boston's Charles River to Chicago's Lakefront path.", created_at=datetime.datetime(2026, 9, 25, 3, 19, 56, tzinfo=TzInfo(0)), session_id=None, observer_id='maya', observed_id='maya', source_ids=['4LF3RrcXQcPP6Mi5RdxPQ', 'aXSriaH1DnQ1EaLD1TVDc', 'jv22v7VqR0n3e2xFLmemU'])]
EV messages: []

```

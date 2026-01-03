#!/usr/bin/env python3
"""
LUCIDITY Beat Map Module
Visualizes AI output degradation patterns across content timeline

Part of LUCIDITY - Universal Multi-Format AI Output Analysis System
Powered by ACTS (Automated Convergence Triangulation System)

Authors: Michael Edwin Robinson (Framework), Terrance Robinson (Execution)
"""

import sys
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass
class BeatMapSegment:
    """Represents one segment in the beat map timeline"""
    start_pos: int
    end_pos: int
    degradation_score: float
    primary_issue: str
    confidence: str
    degradation_breakdown: Dict[str, float]


class LucidityBeatMap:
    """
    Generates visual timeline of degradation patterns
    Shows where and how AI output quality degrades across content
    """
    
    # Color codes for terminal output
    COLORS = {
        'reset': '\033[0m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'orange': '\033[38;5;208m',
        'red': '\033[91m',
        'bold': '\033[1m',
        'dim': '\033[2m'
    }
    
    # Degradation categories (The ROT - 6 categories)
    CATEGORIES = [
        'Repetition',
        'Vagueness', 
        'Intent Decay',
        'Confidence Inflation',
        'Voice Degradation',
        'Entropy Collapse'
    ]
    
    CATEGORY_ABBREV = {
        'Repetition': 'REP',
        'Vagueness': 'VAG',
        'Intent Decay': 'INT',
        'Confidence Inflation': 'CNF',
        'Voice Degradation': 'VOI',
        'Entropy Collapse': 'ENT'
    }
    
    def __init__(self, segments: int = 20, use_color: bool = True):
        """
        Initialize Beat Map generator
        
        Args:
            segments: Number of timeline segments (default 20)
            use_color: Use terminal colors (default True)
        """
        self.segments = segments
        self.use_color = use_color
        self.beat_segments: List[BeatMapSegment] = []
    
    def analyze_content(self, content: str, degradation_data: Dict) -> List[BeatMapSegment]:
        """
        Analyze content and create beat map segments
        
        Args:
            content: Full text content
            degradation_data: ACTS analysis results with degradation scores
            
        Returns:
            List of BeatMapSegment objects
        """
        content_length = len(content)
        segment_size = content_length // self.segments
        
        segments = []
        
        for i in range(self.segments):
            start = i * segment_size
            end = start + segment_size if i < self.segments - 1 else content_length
            
            # Calculate degradation for this segment
            segment_text = content[start:end]
            
            # Simulate degradation scoring (integrate with ACTS here)
            seg_score = self._calculate_segment_degradation(
                segment_text, 
                degradation_data,
                position=i/self.segments
            )
            
            segments.append(BeatMapSegment(
                start_pos=start,
                end_pos=end,
                degradation_score=seg_score['overall'],
                primary_issue=seg_score['primary'],
                confidence=seg_score['confidence'],
                degradation_breakdown=seg_score['breakdown']
            ))
        
        self.beat_segments = segments
        return segments
    
    def _calculate_segment_degradation(self, text: str, data: Dict, position: float) -> Dict:
        """
        Calculate degradation metrics for a text segment
        
        Args:
            text: Segment text
            data: Full degradation data
            position: Position in document (0.0 to 1.0)
            
        Returns:
            Dict with overall score, primary issue, and breakdown
        """
        # This is where ACTS integration happens
        # For demo purposes, using realistic patterns
        
        breakdown = {}
        
        # Repetition tends to cluster
        breakdown['Repetition'] = min(100, len(set(text.split())) / max(1, len(text.split())) * 100)
        
        # Vagueness often front-loaded
        breakdown['Vagueness'] = max(0, 80 - position * 60) if position < 0.5 else 20
        
        # Intent decay back-loaded
        breakdown['Intent Decay'] = min(100, position * 120)
        
        # Confidence inflation periodic
        breakdown['Confidence Inflation'] = 30 + 20 * abs(0.5 - (position % 0.25) * 4)
        
        # Voice degradation late onset
        breakdown['Voice Degradation'] = max(0, (position - 0.7) * 200) if position > 0.7 else 5
        
        # Entropy collapse early
        breakdown['Entropy Collapse'] = max(0, 60 - position * 50)
        
        overall = sum(breakdown.values()) / len(breakdown)
        
        primary = max(breakdown, key=breakdown.get)
        
        confidence = "High" if overall < 30 or overall > 70 else "Medium"
        
        return {
            'overall': overall,
            'primary': primary,
            'confidence': confidence,
            'breakdown': breakdown
        }
    
    def render_ascii(self, width: int = 60) -> str:
        """
        Generate ASCII beat map visualization
        
        Args:
            width: Character width of the timeline
            
        Returns:
            Formatted ASCII beat map string
        """
        if not self.beat_segments:
            return "No beat map data available. Run analyze_content() first."
        
        lines = []
        
        # Header
        lines.append(self._box_line('═', width))
        lines.append(self._box_text('LUCIDITY BEAT MAP ANALYSIS', width))
        lines.append(self._box_line('═', width))
        lines.append(self._box_text('', width))
        
        # Overall timeline
        timeline_bar = self._generate_timeline_bar(width - 4)
        lines.append(self._box_text(f"Document Flow: {timeline_bar}", width))
        lines.append(self._box_text('', width))
        
        # Degradation visualization
        degrad_bar = self._generate_degradation_bar(width - 4)
        lines.append(self._box_text(f"Degradation:   {degrad_bar}", width))
        
        # Spike markers
        spikes = self._find_spikes()
        if spikes:
            spike_line = ' ' * 15
            for spike_pos, spike_pct in spikes:
                marker_pos = int(spike_pos * (width - 20))
                spike_line = spike_line[:marker_pos] + '↑ Spike' + spike_line[marker_pos + 7:]
            lines.append(self._box_text(spike_line, width))
            
            spike_pct_line = ' ' * 15
            for spike_pos, spike_pct in spikes:
                marker_pos = int(spike_pos * (width - 20))
                label = f"@ {int(spike_pct)}%"
                spike_pct_line = spike_pct_line[:marker_pos] + label + spike_pct_line[marker_pos + len(label):]
            lines.append(self._box_text(spike_pct_line, width))
        
        lines.append(self._box_text('', width))
        
        # Category breakdown
        lines.append(self._box_text('Category Breakdown:', width))
        
        for category in self.CATEGORIES:
            abbrev = self.CATEGORY_ABBREV[category]
            avg_score = self._get_average_category_score(category)
            bar = self._generate_category_bar(category, width - 30)
            status = self._get_status(avg_score)
            
            line = f"{abbrev}: {bar} {avg_score:3.0f}% ({status})"
            lines.append(self._box_text(line, width))
        
        lines.append(self._box_text('', width))
        
        # Key findings
        findings = self._generate_findings()
        lines.append(self._box_text(f"🎯 Key Finding: {findings['key']}", width))
        lines.append(self._box_text(f"💡 Recommendation: {findings['rec']}", width))
        
        lines.append(self._box_line('═', width))
        
        return '\n'.join(lines)
    
    def render_html(self) -> str:
        """
        Generate interactive HTML beat map
        
        Returns:
            HTML string with embedded JavaScript visualization
        """
        if not self.beat_segments:
            return "<p>No beat map data available.</p>"
        
        html = """
        <div id="beatmap-container" style="font-family: 'Courier New', monospace; background: #1a1a1a; color: #00ff00; padding: 20px; border-radius: 8px;">
            <h2 style="text-align: center; color: #00ff00; margin-bottom: 20px;">LUCIDITY BEAT MAP</h2>
            
            <div id="timeline" style="margin: 20px 0;">
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <span style="width: 150px;">Overall Flow:</span>
                    <div style="flex: 1; height: 30px; background: #333; border-radius: 4px; overflow: hidden;">
        """
        
        # Generate colored segments
        for i, seg in enumerate(self.beat_segments):
            color = self._get_segment_color_hex(seg.degradation_score)
            width_pct = 100 / len(self.beat_segments)
            
            html += f'''
                        <div style="display: inline-block; width: {width_pct}%; height: 100%; background: {color}; 
                             cursor: pointer;" 
                             title="Segment {i+1}: {seg.degradation_score:.1f}% degradation - {seg.primary_issue}"
                             onmouseover="this.style.opacity='0.7'" 
                             onmouseout="this.style.opacity='1'">
                        </div>
            '''
        
        html += """
                    </div>
                </div>
            </div>
            
            <div id="categories" style="margin: 20px 0;">
        """
        
        # Category bars
        for category in self.CATEGORIES:
            avg = self._get_average_category_score(category)
            abbrev = self.CATEGORY_ABBREV[category]
            
            html += f'''
                <div style="display: flex; align-items: center; margin: 5px 0;">
                    <span style="width: 150px; font-weight: bold;">{abbrev}:</span>
                    <div style="flex: 1; height: 20px; background: #333; border-radius: 4px; overflow: hidden;">
                        <div style="width: {avg}%; height: 100%; background: {self._get_segment_color_hex(avg)};"></div>
                    </div>
                    <span style="width: 100px; text-align: right; margin-left: 10px;">{avg:.0f}% {self._get_status(avg)}</span>
                </div>
            '''
        
        html += """
            </div>
            
            <div id="insights" style="margin-top: 30px; padding: 15px; background: #2a2a2a; border-left: 4px solid #00ff00; border-radius: 4px;">
        """
        
        findings = self._generate_findings()
        html += f'''
                <p style="margin: 5px 0;"><strong>🎯 Key Finding:</strong> {findings['key']}</p>
                <p style="margin: 5px 0;"><strong>💡 Recommendation:</strong> {findings['rec']}</p>
        '''
        
        html += """
            </div>
        </div>
        """
        
        return html
    
    def generate_meeting_summary(self) -> Dict[str, str]:
        """
        Generate concise meeting-ready summary
        
        Returns:
            Dict with 60-second summary, key finding, and action item
        """
        if not self.beat_segments:
            return {
                'summary': 'No analysis available',
                'finding': 'Run analysis first',
                'action': 'Execute LUCIDITY analysis'
            }
        
        avg_degradation = sum(s.degradation_score for s in self.beat_segments) / len(self.beat_segments)
        
        primary_issues = {}
        for seg in self.beat_segments:
            primary_issues[seg.primary_issue] = primary_issues.get(seg.primary_issue, 0) + 1
        
        top_issue = max(primary_issues, key=primary_issues.get)
        
        spikes = self._find_spikes()
        
        findings = self._generate_findings()
        
        summary = f"Analysis of {len(self.beat_segments)} segments shows {avg_degradation:.0f}% average degradation. "
        summary += f"Primary concern: {top_issue}. "
        
        if spikes:
            summary += f"Detected {len(spikes)} degradation spike(s) at "
            summary += ', '.join([f"{int(pos*100)}%" for pos, _ in spikes]) + ". "
        
        return {
            'summary': summary,
            'finding': findings['key'],
            'action': findings['rec']
        }
    
    # Helper methods
    
    def _box_line(self, char: str, width: int) -> str:
        """Generate box border line"""
        return f"╔{'═' * width}╗" if char == '═' else f"╠{'═' * width}╣"
    
    def _box_text(self, text: str, width: int) -> str:
        """Generate boxed text line"""
        padding = width - len(text)
        return f"║ {text}{' ' * padding}║"
    
    def _generate_timeline_bar(self, width: int) -> str:
        """Generate full timeline bar"""
        return f"[{'█' * width}]"
    
    def _generate_degradation_bar(self, width: int) -> str:
        """Generate degradation intensity bar"""
        bar = []
        
        for i, seg in enumerate(self.beat_segments):
            seg_width = width // len(self.beat_segments)
            
            if seg.degradation_score < 25:
                char = '░'
                color = 'green'
            elif seg.degradation_score < 50:
                char = '▒'
                color = 'yellow'
            elif seg.degradation_score < 75:
                char = '▓'
                color = 'orange'
            else:
                char = '█'
                color = 'red'
            
            if self.use_color:
                bar.append(f"{self.COLORS[color]}{char * seg_width}{self.COLORS['reset']}")
            else:
                bar.append(char * seg_width)
        
        return f"[{''.join(bar)}]"
    
    def _generate_category_bar(self, category: str, width: int) -> str:
        """Generate per-category degradation bar"""
        bar = []
        
        for seg in self.beat_segments:
            score = seg.degradation_breakdown.get(category, 0)
            seg_width = max(1, width // len(self.beat_segments))
            
            char = '█' if score > 50 else '░'
            bar.append(char * seg_width)
        
        result = ''.join(bar)[:width]
        result += '░' * (width - len(result))
        
        return f"[{result}]"
    
    def _find_spikes(self, threshold: float = 20.0) -> List[Tuple[float, float]]:
        """Find degradation spikes above threshold"""
        spikes = []
        
        for i, seg in enumerate(self.beat_segments):
            if i == 0:
                continue
            
            prev_score = self.beat_segments[i-1].degradation_score
            diff = seg.degradation_score - prev_score
            
            if diff > threshold:
                position = i / len(self.beat_segments)
                spikes.append((position, position * 100))
        
        return spikes
    
    def _get_average_category_score(self, category: str) -> float:
        """Calculate average score for a degradation category"""
        if not self.beat_segments:
            return 0.0
        
        scores = [seg.degradation_breakdown.get(category, 0) for seg in self.beat_segments]
        return sum(scores) / len(scores)
    
    def _get_status(self, score: float) -> str:
        """Get status label for a score"""
        if score < 25:
            return "Good" if self.use_color else "Good"
        elif score < 50:
            return f"{self.COLORS['yellow']}Caution{self.COLORS['reset']}" if self.use_color else "Caution"
        elif score < 75:
            return f"{self.COLORS['orange']}Warning{self.COLORS['reset']}" if self.use_color else "Warning"
        else:
            return f"{self.COLORS['red']}Alert!{self.COLORS['reset']}" if self.use_color else "Alert!"
    
    def _get_segment_color_hex(self, score: float) -> str:
        """Get hex color for segment based on score"""
        if score < 25:
            return '#00ff00'  # Green
        elif score < 50:
            return '#ffff00'  # Yellow
        elif score < 75:
            return '#ff8800'  # Orange
        else:
            return '#ff0000'  # Red
    
    def _generate_findings(self) -> Dict[str, str]:
        """Generate key findings and recommendations"""
        if not self.beat_segments:
            return {'key': 'No data', 'rec': 'Run analysis'}
        
        # Find highest degradation category
        category_avgs = {cat: self._get_average_category_score(cat) for cat in self.CATEGORIES}
        worst_category = max(category_avgs, key=category_avgs.get)
        worst_score = category_avgs[worst_category]
        
        # Find where degradation peaks
        peak_seg = max(self.beat_segments, key=lambda s: s.degradation_score)
        peak_pos = self.beat_segments.index(peak_seg)
        peak_pct = int((peak_pos / len(self.beat_segments)) * 100)
        
        # Generate finding
        if worst_score > 60:
            finding = f"{worst_category} spikes "
            
            if peak_pct < 30:
                finding += "in early sections"
            elif peak_pct > 70:
                finding += "in final sections"
            else:
                finding += f"at {peak_pct}% mark"
        else:
            finding = f"Moderate {worst_category} detected throughout"
        
        # Generate recommendation
        if worst_category == 'Intent Decay':
            rec = "Apply focused editing to restore original intent"
        elif worst_category == 'Repetition':
            rec = "Remove redundant content and vary phrasing"
        elif worst_category == 'Vagueness':
            rec = "Add specific details and concrete examples"
        elif worst_category == 'Confidence Inflation':
            rec = "Moderate certainty claims with appropriate caveats"
        elif worst_category == 'Voice Degradation':
            rec = "Restore consistent tone and perspective"
        else:  # Entropy Collapse
            rec = "Restructure content to maintain complexity"
        
        return {
            'key': finding,
            'rec': rec
        }


def demo():
    """Run demonstration of Beat Map functionality"""
    
    # Sample degraded AI output
    sample_text = """
    Artificial intelligence is transforming the world. AI is changing everything.
    Machine learning models are very powerful. They can do many things. They are useful
    for various applications. Many people use AI systems. These systems are increasingly
    common. They help with tasks. AI helps people. It's important to understand AI.
    Understanding is key. Knowledge is power. We should learn more. Education matters.
    The future is AI. AI is the future. Technology advances. Progress continues.
    Innovation happens. Change occurs. Things evolve. Development proceeds. Growth happens.
    """ * 5  # Repeat to create longer content
    
    # Mock degradation data (in real use, this comes from ACTS)
    degradation_data = {
        'overall_score': 67.5,
        'categories': {
            'Repetition': 45.2,
            'Vagueness': 78.3,
            'Intent Decay': 52.1,
            'Confidence Inflation': 23.4,
            'Voice Degradation': 34.6,
            'Entropy Collapse': 71.2
        }
    }
    
    print("\n" + "="*70)
    print("LUCIDITY Beat Map - Demonstration Mode")
    print("="*70 + "\n")
    
    # Create beat map
    beatmap = LucidityBeatMap(segments=20, use_color=True)
    
    # Analyze content
    print("Analyzing content...")
    beatmap.analyze_content(sample_text, degradation_data)
    
    # Generate ASCII visualization
    print("\n" + beatmap.render_ascii(width=60))
    
    # Generate meeting summary
    print("\n" + "="*70)
    print("MEETING MODE SUMMARY")
    print("="*70)
    
    summary = beatmap.generate_meeting_summary()
    print(f"\n📊 60-Second Summary:")
    print(f"   {summary['summary']}")
    print(f"\n🎯 Key Finding:")
    print(f"   {summary['finding']}")
    print(f"\n💡 Action Item:")
    print(f"   {summary['action']}")
    
    print("\n" + "="*70 + "\n")
    
    # Save HTML version
    html_output = beatmap.render_html()
    with open('/home/claude/beatmap_demo.html', 'w') as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <title>LUCIDITY Beat Map Demo</title>
    <meta charset="utf-8">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background: #f0f0f0; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
    </style>
</head>
<body>
    <div class="container">
        <h1 style="text-align: center;">LUCIDITY Beat Map - HTML Demo</h1>
        {html_output}
    </div>
</body>
</html>
        """)
    
    print("✅ HTML demo saved to: beatmap_demo.html")
    print("   Open in browser to see interactive visualization\n")


if __name__ == "__main__":
    demo()

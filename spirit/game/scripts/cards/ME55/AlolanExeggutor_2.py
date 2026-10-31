from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class ScaleUpPassive(Passive):
    """If this Pokemon has 6 or more Grass Energy attached, it gets +250 HP."""
    def max_hp_bonus(self, pokemon, carrier):
        if pokemon is not carrier:
            return 0
        count = sum(1 for c in carrier.children
                    if energy_provides_type(c, PokemonTypes.GRASS))
        if count >= 6:
            return 250
        return 0

card = PokemonCardDef(
    guid="471bce2e-f6a6-5904-ac6b-2d7964c4221f",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutor.Name",
    display_name="Alolan Exeggutor",
    searchable_by=["Alolan Exeggutor", "Stage 1", "AlolanExeggutor"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Ability(
            title="Scale Up",
            game_text="If this Pok\u00e9mon has 6 or more Grass Energy attached, it gets +250 HP.",
            passive=ScaleUpPassive(),
        ),
        Attack(
            title="Mega Drain",
            game_text="Heal 50 damage from this Pok\u00e9mon",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=heal_attack(amount=50, target="self"),
        ),
    ],
)